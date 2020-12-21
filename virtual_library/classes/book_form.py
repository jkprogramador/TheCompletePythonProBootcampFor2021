from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    title = StringField(label="Book Name", validators=[DataRequired()])
    author = StringField(label="Book Author", validators=[DataRequired()])
    rating = SelectField(label="Rating",
                         choices=list(range(1, 11)),
                         validators=[DataRequired()],
                         coerce=int)
    submit = SubmitField(label="Add Book")
