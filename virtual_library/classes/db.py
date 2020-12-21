from app import app
from flask_sqlalchemy import SQLAlchemy
import sqlite3

db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"


db.create_all()
# db = sqlite3.connect(database="books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books ( \
# id INTEGER PRIMARY KEY, \
# title VARCHAR(250) NOT NULL UNIQUE, \
# author VARCHAR(250) NOT NULL, \
# rating FLOAT NOT NULL\
# )")
# cursor.execute("INSERT INTO books VALUES (5, 'Psycho', 'Benjamin', 2)")
# db.commit()
