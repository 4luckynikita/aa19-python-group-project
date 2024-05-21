from flask import Blueprint, jsonify, session, request
from flask_login import login_required
from app.models import Review, db
from app.forms import   ReviewForm

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
# def song_reviews(id):
#     """
#     Query for all reviews for a song and returns them in a list of dictionaries
#     """

#     reviews =  Review.query.filter_by(song_id = id)

#     return [review.to_dict() for review in reviews]


# # create a review for an album
@review_routes.route('/albums/<int:id>', methods=["POST"])
@login_required
def create_album_review(id):
    """
        Create a review for an album
    """
    form = ReviewForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        review = Review(
            user_id = session['_user_id'],
            reviewable_type = "Album",
            reviewable_id = id,
            rating = form.data["rating"],
            comment = form.data["comment"],
            album_id = id
        )
        db.session.add(review)
        db.session.commit()
        return review.to_dict()
    return form.errors, 400

# # create a review for a song
@review_routes.route('/songs/<int:id>', methods=["POST"])
@login_required
def create_song_review(id):
    """
        Create a review for a song
    """
    form = ReviewForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        review = Review(
            user_id = session['_user_id'],
            reviewable_type = "Song",
            reviewable_id = id,
            rating = form.data["rating"],
            comment = form.data["comment"],
            song_id = id
        )
        db.session.add(review)
        db.session.commit()
        return review.to_dict()
    return form.errors, 400

# delete a review
@review_routes.route('<int:id>', methods=["DELETE"])
@login_required
def delete_song_review(id):
    """
        Create a review for a song
    """
    review = Review.query.get(id)
    if review.user_id == session['_user_id']:
        db.session.delete(review)
        db.session.commit()
        return 'your review has been deleted'
    return 'you are unauthorized to perform this action', 401
