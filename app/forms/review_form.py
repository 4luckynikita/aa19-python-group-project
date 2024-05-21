from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from wtforms.validators import DataRequired




class ReviewForm(FlaskForm):
    rating = SelectField("rating", choices=[1, 2, 3, 4, 5], validators=[DataRequired()])
    comment = StringField("Comment")
