from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField
from wtforms.validators import DataRequired, NumberRange, Length, URL

class AlbumForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired('Please add a title.'), Length(min=1, max=40, message="Title must be between 1 and 40 characters long.")])
    release_date = DateField('Release Date', validators=[DataRequired("Please provide a release date")])
    description = StringField('Description', validators=[DataRequired("Please add a description"), Length(min=1, max=500, message="Title must be between 1 and 40 characters long.")])
    image_url = StringField('Image URL', validators=[DataRequired('Please provide an Image URL'), URL('Image URL syntax is invalid')])
