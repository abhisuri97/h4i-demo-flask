from flask_wtf import Form
from wtforms import ValidationError
from wtforms.fields import (
    BooleanField,
    IntegerField,
    PasswordField,
    StringField,
    SubmitField,
)
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, EqualTo, InputRequired, Length

class MakeClub(Form):
    name = StringField(
        'Name', validators=[InputRequired(),
                             Length(1, 64)])
    submit = SubmitField('Make Club')

class ReviewClub(Form):
    good = IntegerField(
        'Rating 1-5', validators=[InputRequired()])
    submit = SubmitField('Make Club')
