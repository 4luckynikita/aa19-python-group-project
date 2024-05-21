from flask import Blueprint, jsonify, session
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

# get review by id
@review_routes.route('/<int:id>')
@login_required
def review_by_id(id):
    """
    Query for getting a review by id and returns the review as a dictionary
    """

    review = Review.query.get(id)
    return review.to_dict()

# get all reviews of the current user
@review_routes.route('/current')
@login_required
def current_user_reviews():
    """
    Query for all reviews of the current user and returns them in a list of dictionaries
    """
    id = session['_user_id']
    reviews =  Review.query.filter_by(user_id = id)

    return [review.to_dict() for review in reviews]

# # get all reviews of an album
# @review_routes.route('albums/<int:id>')
# @login_required
# def album_reviews(id):
#     """
#     Query for all reviews for an album and returns them in a list of dictionaries
#     """

#     reviews =  Review.query.filter_by(album_id = id)

#     return [review.to_dict() for review in reviews]

# # get all reviews for a song
# @review_routes.route('songs/<int:id>')
# @login_required
# def album_reviews(id):
#     """
#     Query for all reviews for a song and returns them in a list of dictionaries
#     """

#     reviews =  Review.query.filter_by(song_id = id)

#     return [review.to_dict() for review in reviews]




# # create a review for an album
@review_routes.route('/', methods=["POST"])
def create_review():
     """
        Create a review for a song
    """
