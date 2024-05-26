from flask import Blueprint, request
from app.models import User, db
from app.forms import LoginForm
from app.forms import SignUpForm
from flask_login import current_user, login_user, logout_user, login_required

auth_routes = Blueprint("auth", __name__)


@auth_routes.route("/")
def authenticate():
    print(current_user)
    if current_user.is_authenticated:
        return current_user.to_dict()
    return {"errors": {"message": "Unauthorized"}}, 401


@auth_routes.route("/login", methods=["POST"])
def login():
    form = LoginForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():

        user = User.query.filter(User.email == form.data["email"]).first()
        login_user(user)
        return user.to_dict()
    return form.errors, 401


@auth_routes.route("/logout")
def logout():
    logout_user()
    return {"message": "User logged out"}


@auth_routes.route("/signup", methods=["POST"])
def sign_up():
    form = SignUpForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        user_data = {
            "email": form.data["email"],
            "password": form.data["password"],
            "is_musician": form.data["is_musician"],
            "description": form.data["description"],
            "image_url": form.data["image_url"],
        }

        if form.data["is_musician"]:
            user_data["name"] = form.data["name"]
            user_data["genre"] = form.data["genre"]
        else:
            user_data["username"] = form.data["username"]
            user_data["first_name"] = form.data["first_name"]
            user_data["last_name"] = form.data["last_name"]

        user = User(**user_data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return user.to_dict()
    return form.errors, 401


# @auth_routes.route("/current", methods=["GET"])
# @login_required
# def current_user():
#     return current_user.to_dict(), 200


@auth_routes.route("/unauthorized")
def unauthorized():
    """
    Returns unauthorized JSON when flask-login authentication fails
    """
    return {"errors": {"message": "Unauthorized"}}, 401
