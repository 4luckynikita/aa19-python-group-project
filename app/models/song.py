from datetime import datetime
from .db import db, environment, SCHEMA


class Song(db.Model):
    __tablename__ = "songs"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    album_id = db.Column(db.Integer, db.ForeignKey("albums.id"), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    duration = db.Column(db.Integer, nullable=True)
    image_url = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
    )
