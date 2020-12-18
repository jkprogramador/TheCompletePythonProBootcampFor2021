from flask import Flask, render_template, request
import requests
import sys
import smtplib

MY_EMAIL = ""
MY_EMAIL_USERNAME = ""
MY_EMAIL_PASSWORD = ""

app = Flask(__name__)

try:
    res = requests.get("https://api.npoint.io/43644ec4f0013682fc0d")
    res.raise_for_status()
    posts = res.json()
except ValueError as ex:
    print(ex)
    sys.exit(1)


def send_email(email_msg):
    print(email_msg)
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(user=MY_EMAIL_USERNAME,
    #                      password=MY_EMAIL_PASSWORD)
    #     connection.send_message(
    #         msg=f"Subject:Contact added\n\n{email_msg}",
    #         from_addr=MY_EMAIL, to_addrs=MY_EMAIL)


def send_message(func):
    def contact():
        if request.method == "POST":
            name = request.form["name"]
            email = request.form["email"]
            phone = request.form["phone"]
            message = request.form["message"]
            email_msg = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
            send_email(email_msg)

        return func()

    return contact


@app.route("/")
def home():
    return render_template("index.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
@send_message
def contact():
    return render_template("contact.html", method=request.method)


@app.route("/post/<int:blog_id>")
def get_post(blog_id: int):
    results = [el for el in posts if el["id"] == blog_id]

    if len(results) > 0:
        blog_post = results[0]
        return render_template("post.html", post=blog_post)
    else:
        return '<h1>404 Not Found</h1>', 404


if __name__ == "__main__":
    app.run(debug=True)
