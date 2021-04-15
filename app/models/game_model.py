from . import db
from datetime import datetime


class GameModel(db.Model):
    __tablename__ = "games"

    id = db.Column(db.Integer, primary_key=True)
    game_numbers = db.Column(db.String, nullable=True)
    timestamp = db.Column(db.DateTime(), default=datetime.utcnow, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    owner = db.relationship(
        "UserModel", backref=db.backref("game_list", lazy="joined"), lazy="joined"
    )

    def __repr__(self):
        return f"<class GameModel\n numbers:{self.game_numbers}\n times:{self.timestamp}\n owner_id:{self.user_id}>"
