from flask import Blueprint, request
from marshmallow import fields, validate
from config import db, ma
from models import FoodItem

food_item = Blueprint("food_item", __name__)


class FoodItemSchema(ma.Schema):
    name = fields.Str(required=True, validate=[validate.Length(min=1, max=100)])
    size_grams = fields.Int(required=True)
    serving_size_grams = fields.Int(required=True)
    fat_grams = fields.Int(required=True)
    protien_grams = fields.Int(required=True)
    carbs_grams = fields.Int(required=True)
    exp_date = fields.Date(required=True)
    inventory_id = fields.Int(required=True)

    class Meta:
        fields = (
            "id",
            "name",
            "size_grams",
            "serving_size_grams",
            "fat_grams",
            "protien_grams",
            "carbs_grams",
            "exp_date",
            "inventory_id",
        )


food_item_schema = FoodItemSchema()
food_items_schema = FoodItemSchema(many=True)


@food_item.route("/", methods=["GET"])
def get_all_food_items():
    all_food_items = FoodItem.query.all()
    return food_items_schema.jsonify(all_food_items)


@food_item.route("/<id>", methods=["GET"])
def get_food_item(id):
    food_item = FoodItem.query.get(id)
    return food_item_schema.jsonify(food_item)


@food_item.route("/", methods=["POST"])
def create_food_item():
    if errors := FoodItemSchema().validate(request.json):
        return {"errors": errors}, 422

    new_food_item = FoodItem(
        inventory_id=request.json["inventory_id"],
        name=request.json["name"],
        size_grams=request.json["size_grams"],
        serving_size_grams=request.json["serving_size_grams"],
        fat_grams=request.json["fat_grams"],
        protien_grams=request.json["protien_grams"],
        carbs_grams=request.json["carbs_grams"],
        exp_date=request.json["exp_date"],
    )
    db.session.add(new_food_item)
    db.session.commit()

    return food_item_schema.jsonify(new_food_item)


@food_item.route("/<id>", methods=["PUT"])
def modify_food_item(id):
    food_item = FoodItem.query.get(id)

    food_item.name = request.json["name"] if "name" in request.json else food_item.name
    food_item.size_grams = (
        request.json["size_grams"]
        if "size_grams" in request.json
        else food_item.size_grams
    )
    food_item.serving_size_grams = (
        request.json["serving_size_grams"]
        if "serving_size_grams" in request.json
        else food_item.serving_size_grams
    )
    food_item.fat_grams = (
        request.json["fat_grams"]
        if "fat_grams" in request.json
        else food_item.fat_grams
    )
    food_item.protien_grams = (
        request.json["protien_grams"]
        if "protien_grams" in request.json
        else food_item.protien_grams
    )
    food_item.carbs_grams = (
        request.json["carbs_grams"]
        if "carbs_grams" in request.json
        else food_item.carbs_grams
    )
    food_item.exp_date = (
        request.json["exp_date"] if "exp_date" in request.json else food_item.exp_date
    )
    db.session.commit()

    return food_item_schema.jsonify(food_item)


@food_item.route("/<id>", methods=["DELETE"])
def delete_food_item(id):
    food_item = FoodItem.query.get(id)
    db.session.delete(food_item)
    db.session.commit()
    return food_item_schema.jsonify(food_item)
