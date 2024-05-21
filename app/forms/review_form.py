from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import Review



class ReviewForm(FlaskForm):
    rating = SelectField(choices=[1, 2, 3, 4, 5], validators=[DataRequired()])
    comment = StringField("Comment")
