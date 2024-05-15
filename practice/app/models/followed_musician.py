from datetime import datetime
from .db import db


class FollowedMusician(db.Model):
    __tablename__ = "followed_musicians"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    musician_id = db.Column(db.Integer, db.ForeignKey("musicians.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
