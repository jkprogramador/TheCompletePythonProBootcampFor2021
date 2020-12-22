from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from app import app

db = SQLAlchemy(app=app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.String(4), nullable=False)
    description = db.Column(db.Text, nullable=True)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.Text, nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

    @classmethod
    def get_all(cls) -> list:
        return cls.query.order_by(text(f"{cls.ranking} ASC")).all()

    @classmethod
    def get_highest_rated(cls):
        return cls.query.order_by(text(f"{cls.rating} DESC")).first()

    @classmethod
    def get_lowest_rated(cls):
        return cls.query.order_by(text(f"{cls.rating} ASC")).first()


db.create_all()
