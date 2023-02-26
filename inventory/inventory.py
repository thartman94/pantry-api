from flask import Blueprint, request
from marshmallow import fields, validate
from config import db, ma
from models import Inventory

inventory = Blueprint("inventory", __name__)


class InventorySchema(ma.Schema):
    name = fields.Str(required=True, validate=[validate.Length(min=1, max=100)])
    description = fields.Str(required=True, validate=[validate.Length(min=1, max=250)])
    user_id = fields.Int(required=True)

    class Meta:
        fields = ("id", "name", "user_id", "description")


inventory_schema = InventorySchema()
inventories_schema = InventorySchema(many=True)


@inventory.route("/", methods=["GET"])
def get_all_inventories():
    all_inventories = Inventory.query.all()
    return inventories_schema.jsonify(all_inventories)


@inventory.route("/<id>", methods=["GET"])
def get_inventory(id):
    inventory = Inventory.query.get(id)
    return inventory_schema.jsonify(inventory)


@inventory.route("/", methods=["POST"])
def create_inventory():
    if errors := InventorySchema().validate(request.json):
        return {"errors": errors}, 422

    new_inv = Inventory(
        user_id=request.json["user_id"],
        name=request.json["name"],
        description=request.json["description"],
    )
    db.session.add(new_inv)
    db.session.commit()

    return inventory_schema.jsonify(new_inv)


@inventory.route("/<id>", methods=["PUT"])
def modify_inventory(id):
    inv = Inventory.query.get(id)

    inv.name = request.json["name"] if "name" in request.json else inv.name
    inv.description = (
        request.json["description"]
        if "description" in request.json
        else inv.description
    )

    db.session.commit()
    return inventories_schema.jsonify(inv)


@inventory.route("/<id>", methods=["DELETE"])
def delete_inventory(id):
    inv = Inventory.query.get(id)
    db.session.delete(inv)
    db.session.commit()
    return inventory_schema.jsonify(inv)
