from flask import Flask, render_template
import requests
import sys

app = Flask(__name__)

try:
    res = requests.get("https://api.npoint.io/5abcca6f4e39b4955965")
    res.raise_for_status()
    posts = res.json()
except ValueError as ex:
    print(ex)
    sys.exit(1)


@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route("/post/<int:blog_id>")
def get_post(blog_id: int):
    results = [el for el in posts if el["id"] == blog_id]

    if len(results) > 0:
        blog_post = results[0]
        return render_template("post.html", post=blog_post)
    else:
        return '<h1>404</h1>'


if __name__ == "__main__":
    app.run(debug=True)
