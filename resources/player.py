from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models.player import PlayerModel
from schemas import PlayerSchema


blp = Blueprint("players", __name__, description="Operations on players")

@blp.route("/player/<string:player_id>")
class Player(MethodView):
    @blp.response(200, PlayerSchema)
    def get(self, player_id):
        player = PlayerModel.query.get_or_404(player_id)
        return player

    def delete(self, player_id):
        player = PlayerModel.query.get_or_404(player_id)
        db.session.delete(player)
        db.session.commit()
        return {"message": "Player deleted"}, 200


@blp.route("/player")
class PlayerList(MethodView):
    @blp.response(200, PlayerSchema(many=True))
    def get(self):
        print("all")
        all = PlayerModel.query.all()
        print(all)
        return all

    @blp.arguments(PlayerSchema)
    @blp.response(201, PlayerSchema)
    def post(self, player_data):
        print(player_data)
        player = PlayerModel(**player_data)
        print(player)
        try:
            db.session.add(player)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A player with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the player.")

        return player