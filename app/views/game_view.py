from flask import Blueprint, request, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity

from http import HTTPStatus
from random import sample

from app.models import GameModel
from app.services.webscrapping import get_megasena_result

bp_game = Blueprint("bp_game", __name__, url_prefix="/megasena")


@bp_game.route("/newgame", methods=["POST"])
@jwt_required()
def new_game():

    session = current_app.db.session

    data = request.get_json()

    user_id = get_jwt_identity()

    balls = data["balls"]

    if not balls >= 6 or not balls <= 10:

        return {
            "msg": "Submit a valid number between 6 and 10."
        }, HTTPStatus.BAD_REQUEST

    list_of_balls = sample(range(1, 60), balls)

    number_of_balls = [str(number).zfill(2) for number in list_of_balls]

    game_numbers = ",".join(number_of_balls)

    game: GameModel = GameModel(game_numbers=game_numbers, user_id=user_id)

    session.add(game)
    session.commit()

    return {
        "game": {
            "id_game": game.id,
            "numbers": game.game_numbers,
            "date": game.timestamp,
        }
    }, HTTPStatus.OK


@bp_game.route("/result", methods=["GET"])
@jwt_required()
def get_result():

    result = get_megasena_result()

    return {"result": result}, HTTPStatus.OK


@bp_game.route("/hits", methods=["GET"])
@jwt_required()
def number_of_hits():
    user_id = get_jwt_identity()

    games = (
        GameModel.query.filter_by(user_id=user_id)
        .order_by(GameModel.timestamp.desc())
        .first()
    )

    game_list = games.game_numbers.split(",")

    megasena_result = get_megasena_result()

    result = [result for result in megasena_result if result in game_list]

    return {"number_of_hits": len(result), "hits": result}, HTTPStatus.OK


@bp_game.route("/my-games", methods=["GET"])
@jwt_required()
def my_games():

    user_id = get_jwt_identity()

    game_list = GameModel.query.filter_by(user_id=user_id).all()

    games = [game.game_numbers.split(",") for game in game_list]

    return {"games": games}, HTTPStatus.OK
