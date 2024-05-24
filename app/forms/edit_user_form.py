from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Email, Optional
from app.models import User


class EditUserForm(FlaskForm):
    username = StringField("username", validators=[Optional()])
    email = StringField("email", validators=[Optional()])
    password = StringField("password", validators=[Optional()])
    name = StringField('name', validators=[Optional()])
    first_name = StringField("First Name", validators=[Optional()])
    last_name = StringField("Last Name", validators=[Optional()])
    is_musician = BooleanField("Musician", validators=[Optional()])
    genre = StringField("Genre", validators=[Optional()])
    description = StringField("Description", validators=[Optional()])
    image_url = StringField("Image URL", validators=[Optional()])
