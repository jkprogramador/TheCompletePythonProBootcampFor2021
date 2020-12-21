from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField


class ChangeRatingForm(FlaskForm):
    rating = SelectField(label="New Rating", choices=list(range(1, 11)),
                         coerce=int)
    submit = SubmitField(label="Change Rating")
