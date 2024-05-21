from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Album(db.Model):
    __tablename__ = "albums"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False
    )
    title = db.Column(db.String(120), nullable=False)
    release_date = db.Column(db.Date, nullable=True)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
    )

    user = db.relationship("User", back_populates="albums")
    songs = db.relationship(
        "Song", back_populates="album", cascade="all, delete-orphan"
    )
       # add song and album relationship
    reviews = db.relationship("Review", back_populates="album", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
            "release_date": self.release_date,
            "description": self.description,
            "image_url": self.image_url,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            # "user": self.user.to_dict() if self.user else None,
            # "songs": [song.to_dict() for song in self.songs],
        }
