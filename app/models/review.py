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
    reviewable_id = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer)
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    user = db.relationship("User", back_populates="reviews")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "reviewable_type": self.reviewable_type,
            "reviewable_id": self.reviewable_id,
            "rating": self.rating,
            "comment": self.comment,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            # "user": self.user.to_dict() if self.user else None,
        }
