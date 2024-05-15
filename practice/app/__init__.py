from flask import Flask, request, redirect, render_template, url_for
from .models import db, Musician, Album, Song, Review, User, FollowedMusician, Comment
from .config import Configuration

app = Flask(__name__)

app.config.from_object(Configuration)
db.init_app(app)


@app.route("/")
def home():
    return render_template("base.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=5000)
