from flask import Flask, render_template
import requests
import sys

app = Flask(__name__)

try:
    res = requests.get("https://api.npoint.io/43644ec4f0013682fc0d")
    res.raise_for_status()
    posts = res.json()
except ValueError as ex:
    print(ex)
    sys.exit(1)


@app.route('/')
def home():
    return render_template("index.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


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
