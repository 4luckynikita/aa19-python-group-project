from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Email, ValidationError, Optional
from app.models import User

def user_exists(form, field):
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user:
        raise ValidationError("Email address is already in use.")

def username_exists(form, field):
    username = field.data
    user = User.query.filter(User.username == username).first()
    if user:
        raise ValidationError("Username is already in use.")

class SignUpForm(FlaskForm):
    username = StringField("username", validators=[Optional(), username_exists])
    email = StringField("email", validators=[DataRequired(), user_exists])
    password = StringField("password", validators=[DataRequired()])
    name = StringField('name', validators=[Optional()])
    first_name = StringField("first_name", validators=[Optional()])
    last_name = StringField("last_name", validators=[Optional()])
    is_musician = BooleanField("is_musician")
    genre = StringField("genre", validators=[Optional()])
    description = StringField("description", validators=[DataRequired()])
    image_url = StringField("image_url", validators=[DataRequired()])
