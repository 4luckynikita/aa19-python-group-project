from flask import Blueprint, jsonify, request
from app.models import User, db, Album, Song, Review
from app.forms.album_form import AlbumForm
from flask_login import login_required, current_user
from datetime import datetime
album_routes = Blueprint('albums', __name__)

# Get all albums with songs and reviews
@album_routes.route("/")
def albums():
    fetched_albums = Album.query.all()
    album_array = []
    for album in fetched_albums:
        album_dict = album.to_dict()
        album_songs = Song.query.filter(Song.album_id == album.id)
        album_dict['songs'] = [song.to_dict() for song in album_songs]
        album_reviews = Review.query.filter(Review.album_id == album.id)
        album_dict['reviews'] = [review.to_dict() for review in album_reviews]
        album_musician = User.query.filter(User.id == album.user_id)
        album_dict['musician'] = [musician.to_dict() for musician in album_musician]
        album_array.append(album_dict)
    return {'albums':album_array}

# Get specific album with songs and musician info
@album_routes.route("/<int:id>")
def album_by_id(id):
    found_album = Album.query.get(id)
    album_with_songs = []
    if found_album:
        album_dict = found_album.to_dict()
        album_songs = Song.query.filter(Song.album_id == found_album.id)
        album_dict['songs'] = [song.to_dict() for song in album_songs]
        album_reviews = Review.query.filter(Review.album_id == found_album.id)
        album_dict['reviews'] = [review.to_dict() for review in album_reviews]
        album_musician = User.query.filter(User.id == found_album.user_id)
        album_dict['musician'] = [musician.to_dict() for musician in album_musician]
        album_with_songs.append(album_dict)
        return jsonify(album_with_songs)
    else:
        return {  "message": "Album could not be found" }, 404
    
# Delete an album with songs, commented out login required temporarily
@album_routes.route("/<int:id>", methods=["DELETE"])
@login_required
def delete_album(id):
    found_album = Album.query.get(id)
    if not found_album:
        return {  "message": "Album could not be found" }, 404
    if found_album.user_id != current_user.id:
        return {"message": "This is not your album"}, 401
    else:
        db.session.delete(found_album)
        db.session.commit()
        return {  "message": "Album deleted successfully" }, 200
    
# Create an album, commented out all user specific methods temporarily
@album_routes.route("/", methods=["POST"])
@login_required
def create_album():
    form = AlbumForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        new_album = Album(
            title = form.data["title"],
            release_date = form.data["release_date"],
            description = form.data["description"],
            image_url = form.data["image_url"],
            user_id = current_user.id
        )
        db.session.add(new_album)
        db.session.commit()
        return new_album.to_dict(), 200
    return form.errors, 400

# Update an album, all user specific methods commented out temporarily
@album_routes.route("/<int:id>", methods=["PUT"])
@login_required
def update_album(id):
    form = AlbumForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    old_album = Album.query.get(id)
    if not old_album:
        return {"message": "Album could not be found"}, 404
    if old_album.user_id != current_user.id:
        return {"message": "This is not your album"}, 401
    if form.validate_on_submit():
        old_album.title = form.data["title"]
        old_album.release_date = form.data["release_date"]
        old_album.description = form.data["description"]
        old_album.image_url = form.data["image_url"]
        db.session.commit()
        return old_album.to_dict(), 200
    return form.errors, 400