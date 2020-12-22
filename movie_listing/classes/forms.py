from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import DecimalField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class RateMovieForm(FlaskForm):
    rating = DecimalField(label="Your rating out of 10, e.g. 7.5",
                          validators=[DataRequired(),
                                      NumberRange(min=1, max=10)])
    review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Done")


class AddMovieForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")
