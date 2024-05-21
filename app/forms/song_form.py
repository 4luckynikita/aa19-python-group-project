from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, TimeField, URLField, IntegerField
from wtforms.validators import DataRequired


class SongForm(FlaskForm):
    title = StringField("title", validators=[DataRequired()])
    duration = IntegerField("release date", validators=[DataRequired()])
    image_url = URLField("image url", validators=[DataRequired()])
