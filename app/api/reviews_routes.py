from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Review

review_routes = Blueprint('reviews', __name__)

# get all reviews
@review_routes.route('/')
@login_required
def reviews():
    """
    Query for all reviews and returns them in a list of dictionaries
    """
    reviews = Review.query.all()
    return [review.to_dict() for review in reviews]
