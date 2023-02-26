from flask import Blueprint, request
from marshmallow import fields, validate
from datetime import datetime
from config import db, ma
from models import User

user = Blueprint("user", __name__)


class UserSchema(ma.Schema):
    first_name = fields.Str(required=True, validate=[validate.Length(min=1, max=100)])
    last_name = fields.Str(required=True, validate=[validate.Length(min=1, max=100)])
    email = fields.Str(required=True, validate=[validate.Length(min=1, max=100)])

    class Meta:
        fields = ("id", "first_name", "last_name", "email", "date_joined")


user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user.route("/<id>", methods=["GET"])
def get_user(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)


@user.route("/", methods=["GET"])
def get_all_users():
    all_users = User.query.all()
    return users_schema.jsonify(all_users)


@user.route("/", methods=["POST"])
def create_user():
    if errors := UserSchema().validate(request.json):
        return {"errors": errors}, 422

    new_user = User(
        first_name=request.json["first_name"],
        last_name=request.json["last_name"],
        email=request.json["email"],
        date_joined=datetime.now(),
    )
    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)


@user.route("/<id>", methods=["PUT"])
def modify_user(id):
    user = User.query.get(id)

    user.first_name = (
        request.json["first_name"] if "first_name" in request.json else user.first_name
    )
    user.last_name = (
        request.json["last_name"] if "last_name" in request.json else user.last_name
    )
    user.email = request.json["email"] if "email" in request.json else user.email

    db.session.commit()
    return user_schema.jsonify(user)


@user.route("/<id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return user_schema.jsonify(user)
