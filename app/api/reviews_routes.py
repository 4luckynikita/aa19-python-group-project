from flask import Blueprint, jsonify, session, request
from flask_login import login_required, current_user
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
    if review:
        return review.to_dict()
    return 'OOps! Looks like this review does not exist', 404

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
            rating = form.data["rating"],
            comment = form.data["comment"],
            album_id = id
        )
        db.session.add(review)
        db.session.commit()
        return review.to_dict()
    return form.errors, 400

# update a review
@review_routes.route('/<int:id>', methods=["PUT"])
@login_required
def update_review(id):
    """
        Update a review
    """
    review = Review.query.get(id)
    if review.user_id != current_user.id:
        return 'you are unauthorized to perform this action', 401
    form = ReviewForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        review.rating = form.data["rating"]
        review.comment = form.data["comment"]
        db.session.commit()
        return review.to_dict()

    return form.errors

# delete a review
@review_routes.route('/<int:id>', methods=["DELETE"])
@login_required
def delete_song_review(id):
    """
        Create a review for a song
    """
    review = Review.query.get(id)
    if review == None:
        return 'OOps! Looks like this review does not exist', 404

    if review.user_id == int(session['_user_id']):
        db.session.delete(review)
        db.session.commit()
        return 'your review has been deleted'
    return 'you are unauthorized to perform this action', 401
