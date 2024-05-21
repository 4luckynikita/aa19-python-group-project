from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Review(db.Model):
    __tablename__ = "reviews"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False
    )
    reviewable_type = db.Column(db.String(50), nullable=False)
    # add song and album column
    album_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("albums.id")))
    # add song and album column
    rating = db.Column(db.Integer)
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    user = db.relationship("User", back_populates="reviews")
    # add song and album relationship
    album = db.relationship("Album", back_populates="reviews")


    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "reviewable_type": self.reviewable_type,
            "rating": self.rating,
            "comment": self.comment,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            # add song and album relationship
            "album_id": self.album_id
            # "user": self.user.to_dict() if self.user else None,
        }
