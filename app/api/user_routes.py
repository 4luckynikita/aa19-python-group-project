from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import User, db
from app.forms import LoginForm
from app.forms import SignUpForm, EditUserForm

user_routes = Blueprint("users", __name__)


@user_routes.route("/", methods=["GET"])
@login_required
def users():
    users = User.query.all()
    return {"users": [user.to_dict() for user in users]}


@user_routes.route("/<int:id>", methods=["GET"])
@login_required
def user(id):
    user = User.query.get(id)
    return user.to_dict()


@user_routes.route("/new_user", methods=["POST"])
def create_user():
    form = SignUpForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        new_user = User(
            username=form.data["username"],
            email=form.data["email"],
            password=form.data["password"],
            first_name=form.data["first_name"],
            last_name=form.data["last_name"],
            is_musician=form.data["is_musician"],
            genre=form.data["genre"],
            description=form.data["description"],
            image_url=form.data["image_url"],
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user.to_dict(), 201
    return form.errors, 401


@user_routes.route("/update/<int:id>", methods=["PUT"])
@login_required
def update_user(id):
    user = User.query.get(id)
    if user.id != current_user.id:
        return {"errors": {"message": "Unauthorized"}}, 401

    form = EditUserForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        if form.data["username"]:
            user.username = form.data["username"]
        if form.data["email"]:
            user.email = form.data["email"]
        if form.data["password"]:
            user.password = form.data["password"]
        if form.data["first_name"]:
            user.first_name = form.data["first_name"]
        if form.data["last_name"]:
            user.last_name = form.data["last_name"]
        user.is_musician = form.data["is_musician"]
        if form.data["genre"]:
            user.genre = form.data["genre"]
        if form.data["description"]:
            user.description = form.data["description"]
        if form.data["image_url"]:
            user.image_url = form.data["image_url"]
        db.session.commit()
        return user.to_dict(), 200
    return form.errors, 401


@user_routes.route("/delete/<int:id>", methods=["DELETE"])
@login_required
def delete_user(id):
    user = User.query.get(id)
    if user.id != current_user.id:
        return {"errors": {"message": "Unauthorized"}}, 401

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"}), 200
