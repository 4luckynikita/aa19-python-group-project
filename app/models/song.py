from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Song(db.Model):
    __tablename__ = "songs"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    album_id = db.Column(
        db.Integer,
        db.ForeignKey(add_prefix_for_prod("albums.id"), ondelete="CASCADE"),
        nullable=False,
    )
    title = db.Column(db.String(120), nullable=False)
    duration = db.Column(db.Integer, nullable=True)
    image_url = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
    )

    album = db.relationship("Album", back_populates="songs")

    def to_dict(self):
        return {
            "id": self.id,
            "album_id": self.album_id,
            "title": self.title,
            "duration": self.duration,
            "image_url": self.image_url,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            # "album": self.album.to_dict() if self.album else None,
        }
