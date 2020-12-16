from flask import Flask, render_template
from markupsafe import escape
import random
import datetime as dt
import requests

app = Flask(__name__)


def make_bold(func):
    def wrapper_function():
        result = func()
        return f"<b>{result}</b>"

    return wrapper_function


def make_emphasis(func):
    def wrapper_function():
        result = func()
        return f"<em>{result}</em>"

    return wrapper_function


def make_underline(func):
    def wrapper_function():
        result = func()
        return f"<u>{result}</u>"

    return wrapper_function


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = dt.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/card")
def card():
    return render_template("card.html")


@app.route("/cv")
def cv():
    return render_template("cv.html")


@app.route("/hello")
def hello_word():
    return "<h1>Hello World!</h1>"


@app.route("/guess/<name>")
def guess(name: str):
    name = escape(name)
    agify_res = requests.get(f"https://api.agify.io/?name={name}")
    agify_res.raise_for_status()
    age = agify_res.json()["age"]
    genderize_res = requests.get(f"https://api.genderize.io/?name={name}")
    genderize_res.raise_for_status()
    gender = genderize_res.json()["gender"]

    return render_template("guess.html", name=name, age=age, gender=gender)


@app.route("/blog")
def blog():
    res = requests.get("https://api.npoint.io/5abcca6f4e39b4955965")
    res.raise_for_status()
    try:
        all_posts = res.json()

        return render_template("blog.html", posts=all_posts)
    except ValueError as ex:
        print(ex)

        return ""


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def say_bye():
    return "Goodbye!"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {escape(name)} {escape(number)}!"


if "__main__" == __name__:
    app.run(debug=True)
