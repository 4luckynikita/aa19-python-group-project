from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, ValidationError, Optional, Regexp
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
    username = StringField("username", validators=[Optional(), Length(min=3, max=25), username_exists])
    email = StringField("email", validators=[DataRequired(), Email(), Length(min=6, max=255), Regexp(r'^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$'), user_exists])
    password = PasswordField("password", validators=[DataRequired(), Length(min=8, max=255)])
    name = StringField('name', validators=[Optional(), Length(min=1, max=100)])
    first_name = StringField("first_name", validators=[Optional(), Length(min=1, max=50)])
    last_name = StringField("last_name", validators=[Optional(), Length(min=1, max=50)])
    is_musician = BooleanField("is_musician")
    genre = StringField("genre", validators=[Optional(), Length(min=1, max=50)])
    description = TextAreaField("description", validators=[DataRequired(), Length(min=10, max=1000)])
    image_url = StringField("image_url", validators=[DataRequired(), Length(max=255)])
