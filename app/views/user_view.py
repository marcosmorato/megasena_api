from flask import Blueprint, request, current_app
from http import HTTPStatus

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)

from datetime import timedelta

from app.models import UserModel

bp_user = Blueprint("bp_user", __name__)


@bp_user.route("/register", methods=["POST"])
def create_user():

    session = current_app.db.session

    data = request.get_json()
    try:
        email = data["email"]
        password = data["password"]
        first_name = data["first_name"]
        last_name = data["last_name"]
    except KeyError:
        return {"msg": "verify the body of the request"}, HTTPStatus.BAD_REQUEST

    check_email = UserModel.query.filter_by(email=email).first()

    if check_email:
        return {"msg": "Email already exists"}, HTTPStatus.BAD_REQUEST

    new_user = UserModel(
        email=email,
        first_name=first_name,
        last_name=last_name,
    )
    new_user.password = password

    session.add(new_user)
    session.commit()

    access_token = create_access_token(
        identity=new_user.id, expires_delta=timedelta(days=7)
    )
    fresh_token = create_access_token(
        identity=new_user.id, expires_delta=timedelta(days=14), fresh=True
    )

    return {
        "user": {
            "first_name": new_user.first_name,
            "last_name": new_user.last_name,
            "email": new_user.email,
            "access_token": access_token,
            "fresh_token": fresh_token,
        }
    }, HTTPStatus.CREATED


@bp_user.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    try:
        email = data["email"]
        password = data["password"]
    except KeyError:
        return {"error": "Insert Email/Password"}, HTTPStatus.BAD_REQUEST

    found_user: UserModel = UserModel.query.filter_by(email=email).first()

    if not found_user or not found_user.check_password(password):
        return {"error": "Email or Password incorrect"}, HTTPStatus.BAD_REQUEST

    access_token = create_access_token(
        identity=found_user.id, expires_delta=timedelta(days=365)
    )
    fresh_token = create_access_token(
        identity=found_user.id, fresh=True, expires_delta=timedelta(days=730)
    )

    return {"access_token": access_token, "fresh_token": fresh_token}, HTTPStatus.OK


@bp_user.route("/users", methods=["PATCH"])
@jwt_required()
def edit_user():

    session = current_app.db.session

    user_id = get_jwt_identity()

    body: dict = request.get_json()

    check_email = UserModel.query.filter_by(email=body.get("email")).first()

    if check_email:
        return {"msg": "Email already exists"}, HTTPStatus.BAD_REQUEST

    found_user: UserModel = UserModel.query.get(user_id)

    for key, value in body.items():
        setattr(found_user, key, value)

    session.add(found_user)
    session.commit()

    return {
        "user": {
            "email": found_user.email,
            "first_name": found_user.first_name,
            "last_name": found_user.last_name,
        }
    }, HTTPStatus.OK


@bp_user.route("/users", methods=["DELETE"])
@jwt_required()
def delete_user():

    session = current_app.db.session

    user_id = get_jwt_identity()

    found_user = UserModel.query.filter_by(id=user_id).first()

    session.delete(found_user)
    session.commit()

    return {}, HTTPStatus.NO_CONTENT


@bp_user.route("/refresh", methods=["GET"])
@jwt_required(fresh=True)
def refresh():
    user_id = get_jwt_identity()

    refresh_token = create_refresh_token(
        identity=user_id, expires_delta=timedelta(days=14)
    )

    return {"refresh_token": refresh_token}, HTTPStatus.OK
