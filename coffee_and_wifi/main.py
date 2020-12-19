from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.html5 import URLField, TimeField
from wtforms.validators import DataRequired, URL
import csv
import datetime as dt

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField(label="Cafe Location on Google Maps (URL)",
                        validators=[DataRequired(), URL()])
    open_time = TimeField(label="Opening Time e.g. 8AM",
                          validators=[DataRequired()])
    closing_time = TimeField(label="Closing Time e.g. 5:30PM",
                             validators=[DataRequired()])
    coffee_rating = SelectField(label="Coffee Rating",
                                choices=[(i, i * "☕") for i in range(1, 6)],
                                validators=[DataRequired()])
    wifi_rating = SelectField(label="Wi-Fi Strength Rating",
                              choices=[(i, i * "💪") for i in range(1, 6)],
                              validators=[DataRequired()])
    power_rating = SelectField(label="Power Socket Rating",
                               choices=[(i, i * "🔌") for i in range(1, 6)],
                               validators=[DataRequired()])
    submit = SubmitField('Submit')


# ---------------------------------------------------------------------------

def save_cafe_data(cafe: str, location: str, open_time: dt.time,
                   closing_time: dt.time,
                   coffee_rating: str, wifi_rating: str, power_rating: str):
    with open("cafe-data.csv", mode="a", newline='', encoding="utf-8") as file:
        csv.writer(file).writerow(
            [cafe, location,
             open_time.strftime("%I:%M%p"),
             closing_time.strftime("%I:%M%p"),
             int(coffee_rating) * "☕",
             int(wifi_rating) * "💪", int(power_rating) * "🔌"])


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        save_cafe_data(cafe=form.cafe.data, location=form.location.data,
                       open_time=form.open_time.data,
                       closing_time=form.closing_time.data,
                       coffee_rating=form.coffee_rating.data,
                       wifi_rating=form.wifi_rating.data,
                       power_rating=form.power_rating.data)
        return redirect(location=url_for("cafes"))

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
