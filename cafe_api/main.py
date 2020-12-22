from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.sqltypes import Boolean
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self) -> dict:
        return {column.name: getattr(self, column.name) for column in
                self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def get_random_cafe():
    all_cafes = Cafe.query.all()
    random_cafe = random.choice(all_cafes)

    return jsonify({
        "cafe": random_cafe.to_dict()
    })


@app.route("/all")
def get_all_cafes():
    all_cafes = Cafe.query.all()

    return jsonify({
        "cafe": [cafe.to_dict() for cafe in all_cafes]
    })


@app.route("/search")
def search():
    location = request.args.get("loc")

    if location is not None:
        cafe = Cafe.query.filter_by(location=location).first()

        if cafe:
            return jsonify(cafe=cafe.to_dict())
        else:
            return jsonify(
                error={
                    "Not Found": "Sorry, we don't have a cafe at that location."
                }
            ), 404

    return "Bad Request", 400


@app.route("/add", methods=["POST"])
def add_cafe():
    post_data = {}

    for column in Cafe.__table__.columns:
        if "id" == column.name:
            continue

        field_value = request.form.get(column.name)

        if field_value is None:
            return "Bad Request", 400

        if isinstance(column.type, Boolean):
            field_value = bool(int(field_value))

        post_data[column.name] = field_value

    cafe = Cafe(**post_data)
    db.session.add(cafe)
    db.session.commit()

    return jsonify(response={"success": "Successfully added new cafe."})


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id: int):
    new_price = request.args.get("new_price")

    if new_price is not None:
        cafe = Cafe.query.get(cafe_id)

        if cafe is None:
            return jsonify(error={
                "Not Found": "Sorry a cafe with that id was not found in the database."}), 404

        cafe.coffee_price = new_price
        db.session.commit()

        return jsonify(success="Successfully updated the price.")

    return "Bad Request", 400


@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def remove_cafe(cafe_id: int):
    api_key = request.args.get("api-key")

    if api_key is not None:

        if "TopSecretAPIKey" != api_key:
            return jsonify(
                error="Sorry, that's not allowed. Make sure you have the correct api-key."), 403

        cafe = Cafe.query.get(cafe_id)

        if cafe is None:
            return jsonify(error={
                "Not Found": "Sorry a cafe with that id was not found in the database."}), 404

        db.session.delete(cafe)
        db.session.commit()

        return jsonify(success="The cafe was successfully removed.")

    return "Bad Request", 400


if __name__ == '__main__':
    app.run(debug=True)
