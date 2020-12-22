from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from classes.forms import RateMovieForm, AddMovieForm
from classes.tmdb_api import get_movies, get_movie

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
Bootstrap(app)

from db import db, Movie


@app.route("/")
def home():
    movies = Movie.get_all()

    return render_template("index.html", movies=movies)


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id: int):
    form = RateMovieForm()

    if form.validate_on_submit():
        movie = Movie.query.get(id)
        movie.rating = form.rating.data
        movie.review = form.review.data

        for a_movie in Movie.get_all():
            if movie.rating > a_movie.rating:
                movie.ranking = a_movie.ranking
                a_movie.ranking += 1
                break

        db.session.commit()

        return redirect(location=url_for("home"))

    return render_template("edit.html", form=form)


@app.route("/delete/<int:id>")
def delete(id: int):
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()

    return redirect(location=url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()

    if form.validate_on_submit():
        title = form.title.data
        movies = get_movies(title)

        return render_template("select.html", movies=movies)

    return render_template("add.html", form=form)


@app.route("/create/<int:id>")
def create(id: int):
    tmdb_movie = get_movie(id)
    lowest_rated_movie = Movie.get_lowest_rated()
    movie = Movie(
        title=tmdb_movie["title"],
        year=tmdb_movie["year"],
        description=tmdb_movie["description"],
        ranking=lowest_rated_movie.ranking + 1,
        img_url=tmdb_movie["img_url"]
    )
    db.session.add(movie)
    db.session.commit()

    return redirect(location=url_for("edit", id=movie.id))
