from flask import Flask
from markupsafe import escape

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
def hello_word():
    return "<h1>Hello World!</h1>"


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
