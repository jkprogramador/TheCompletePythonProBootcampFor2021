from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from classes.book_form import BookForm
from classes.change_rating_form import ChangeRatingForm

app = Flask(__name__)
app.secret_key = "TG@bG<>&caPfM/5</|zt3yVp-by16O)HvK(j-J]W@Pkt%<2n_1)^;pe-}t^Mab8L"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
Bootstrap(app)

from classes.db import db, Book


@app.route('/')
def home():
    all_books = Book.query.all()

    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookForm()

    if form.validate_on_submit():
        book = Book(title=form.title.data, author=form.author.data,
                    rating=form.rating.data)
        db.session.add(book)
        db.session.commit()

        return redirect(location=url_for("home"))

    return render_template("add.html", form=form)


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id: int):
    form = ChangeRatingForm()

    if form.validate_on_submit():
        a_book = Book.query.get(id)
        a_book.rating = form.rating.data
        db.session.commit()

        return redirect(location=url_for("home"))
    a_book = Book.query.get(id)

    return render_template("edit.html", book=a_book, form=form)

@app.route("/delete/<int:id>")
def delete(id: int):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()

    return redirect(location=url_for("home"))
