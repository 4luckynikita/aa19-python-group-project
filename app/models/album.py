from datetime import datetime
from .db import db, environment, SCHEMA


class Album(db.Model):
    __tablename__ = "albums"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    musician_id = db.Column(db.Integer, db.ForeignKey("musicians.id"), nullable=False)
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
