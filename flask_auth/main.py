from flask import Flask, render_template, request, url_for, redirect, flash, \
    send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask_login import UserMixin, login_user, LoginManager, login_required, \
    current_user, logout_user

app = Flask(__name__)

app.config[
    'SECRET_KEY'] = b'\xe3\xda\xfdP<\x08\xf2\xa0\xd5\x08\xda\xfb\x93\x0e\xd3\x97'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["UPLOAD_FOLDER"] = "static"
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    print(user_id)
    return User.query.get(int(user_id))


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Line below only required once, when creating DB.
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if "POST" == request.method:
        email = request.form.get("email")
        name = request.form.get("name")
        user = User.query.filter_by(email=email).first()

        if user:
            flash("The entered email already exists.")
        else:
            password = generate_password_hash(
                password=request.form.get("password"), method="pbkdf2:sha256",
                salt_length=8)
            new_user = User(
                email=email,
                name=name,
                password=password
            )

            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)

            return redirect(location=url_for("secrets"))

    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if "POST" == request.method:
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()

        if user is None:
            flash("Invalid credentials.")
        else:
            if check_password_hash(pwhash=user.password, password=password):
                login_user(user)

                return redirect(location=url_for("secrets"))

            flash("Invalid credentials.")

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()

    return redirect(location=url_for("home"))


@app.route('/download')
@login_required
def download():
    return send_from_directory(directory=app.config["UPLOAD_FOLDER"],
                               filename="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
