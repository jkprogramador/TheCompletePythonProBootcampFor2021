from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields.html5 import EmailField
from wtforms import PasswordField
from wtforms.validators import DataRequired
from wtforms.validators import Email
from wtforms.validators import Length


class LoginForm(FlaskForm):
    email = EmailField(label="Email", validators=[
        DataRequired(),
        Email(message="Please enter a valid email.")
    ])
    password = PasswordField(label="Password", validators=[
        DataRequired(),
        Length(
            min=8,
            message="Password must contain at least 8 alphanumeric characters.")
    ])
    submit = SubmitField(label="Submit")
