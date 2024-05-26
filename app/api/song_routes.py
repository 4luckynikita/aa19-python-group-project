from flask import Blueprint, jsonify, session, request
from flask_login import login_required, current_user
from app.models import Song, db
from app.forms import SongForm

song_routes = Blueprint('songs', __name__)


# create song by album id
@song_routes.route('/albums/<int:id>', methods=["POST"])
@login_required
def create_song(id):
    """
        Create a review for an album
    """
    form = SongForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        new_song = Song(
            album_id = id,
            title = form.data["title"],
            duration = form.data["duration"],
            image_url = form.data["image_url"]
        )
        db.session.add(new_song)
        db.session.commit()
        return new_song.to_dict()
    return form.errors, 400


# delete a song
@song_routes.route('/<int:id>', methods=["DELETE"])
@login_required
def delete_song_review(id):
    """
        delete a song
    """
    song = Song.query.get(id)
    if song == None:
        return 'OOps! Looks like this song does not exist', 404


    db.session.delete(song)
    db.session.commit()
    return 'your song has been deleted'
