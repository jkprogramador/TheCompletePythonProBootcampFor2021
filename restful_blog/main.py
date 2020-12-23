from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime as dt

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    @classmethod
    def get_all(cls) -> list:
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id: int):
        return BlogPost.query.get(id)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = BlogPost.get_all()

    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = BlogPost.get_by_id(index)

    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods=["GET", "POST"])
def create_post():
    form = CreatePostForm()

    if form.validate_on_submit():
        blog_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            author=form.author.data,
            body=form.body.data,
            img_url=form.img_url.data,
            date=dt.datetime.now().strftime("%B %d, %Y")
        )
        db.session.add(blog_post)
        db.session.commit()

        return redirect(location=url_for("get_all_posts"))

    return render_template("make-post.html", form=form, title="New Post")


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id: int):
    blog_post = BlogPost.query.get(post_id)
    form = CreatePostForm(
        title=blog_post.title,
        subtitle=blog_post.subtitle,
        author=blog_post.author,
        img_url=blog_post.img_url,
        body=blog_post.body
    )
    if form.validate_on_submit():
        blog_post.title = form.title.data
        blog_post.subtitle = form.subtitle.data
        blog_post.author = form.author.data
        blog_post.img_url = form.img_url.data
        blog_post.body = form.body.data
        db.session.commit()

        return redirect(location=url_for("get_all_posts"))

    return render_template("make-post.html", form=form, title="Edit Post")


@app.route("/delete/<int:post_id>")
def delete_post(post_id: int):
    blog_post = BlogPost.query.get(post_id)
    db.session.delete(blog_post)
    db.session.commit()

    return redirect(location=url_for("get_all_posts"))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
