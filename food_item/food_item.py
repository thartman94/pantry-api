from flask import Blueprint, request
from flask_cors import cross_origin
from marshmallow import fields, validate
from config import db, ma
from models import FoodItem
import datetime

food_item = Blueprint("food_item", __name__)


class FoodItemSchema(ma.Schema):
    name = fields.Str(required=True, validate=[validate.Length(min=1, max=100)])
    brand = fields.Str(required=True, validate=[validate.Length(min=1, max=100)])
    size = fields.Int(required=True)
    serving_size = fields.Int(required=True)
    calories = fields.Int(required=True)
    fat = fields.Int(required=True)
    protien = fields.Int(required=True)
    carbs = fields.Int(required=True)
    exp_date = fields.Date(required=True)

    class Meta:
        fields = (
            "id",
            "name",
            "brand",
            "size",
            "serving_size",
            "calories",
            "fat",
            "protien",
            "carbs",
            "exp_date",
        )


food_item_schema = FoodItemSchema()
food_items_schema = FoodItemSchema(many=True)


@food_item.route("/", methods=["GET"])
@cross_origin()
def get_all_food_items():
    all_food_items = FoodItem.query.all()
    response = food_items_schema.jsonify(all_food_items)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return food_items_schema.jsonify(all_food_items)


@food_item.route("/<id>", methods=["GET"])
@cross_origin()
def get_food_item(id):
    food_item = FoodItem.query.get(id)
    return food_item_schema.jsonify(food_item)


@food_item.route("/", methods=["POST"])
@cross_origin()
def create_food_item():
    multiple_items = type(request.json) == list

    if errors := FoodItemSchema(many=multiple_items).validate(request.json):
        return {"errors": errors}, 422

    res = []
    for item in request.json if multiple_items else [request.json]:
        date = item["exp_date"].split("-")
        new_food_item = FoodItem(
            **{
                **item,
                "exp_date": datetime.date(int(date[0]), int(date[1]), int(date[2])),
            }
        )
        db.session.add(new_food_item)
        res.append(new_food_item)

    db.session.commit()
    return food_items_schema.jsonify(res)


@food_item.route("/<id>", methods=["PUT"])
@cross_origin()
def modify_food_item(id):
    food_item = FoodItem.query.get(id)
    if not food_item:
        return {"error": "Item not found"}, 404

    food_item.name = request.json["name"] if "name" in request.json else food_item.name
    food_item.brand = (
        request.json["brand"] if "brand" in request.json else food_item.brand
    )
    food_item.size = request.json["size"] if "size" in request.json else food_item.size
    food_item.calories = (
        request.json["calories"] if "calories" in request.json else food_item.calories
    )
    food_item.serving_size = (
        request.json["serving_size"]
        if "serving_size" in request.json
        else food_item.serving_size
    )
    food_item.fat = request.json["fat"] if "fat" in request.json else food_item.fat
    food_item.protien = (
        request.json["protien"] if "protien" in request.json else food_item.protien
    )
    food_item.carbs = (
        request.json["carbs"] if "carbs" in request.json else food_item.carbs
    )
    food_item.exp_date = (
        request.json["exp_date"] if "exp_date" in request.json else food_item.exp_date
    )
    db.session.commit()

    return food_item_schema.jsonify(food_item)


@food_item.route("/<id>", methods=["DELETE"])
@cross_origin()
def delete_food_item(id):
    food_item = FoodItem.query.get(id)
    if not food_item:
        return {"error": "Item not found"}, 404

    db.session.delete(food_item)
    db.session.commit()
    return food_item_schema.jsonify(food_item)
