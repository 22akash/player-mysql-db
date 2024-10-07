from db import db


class PlayerModel(db.Model):
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    sport = db.Column(db.String(80), nullable=False)
    country = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
