from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class TweetForm(FlaskForm):
    tweet = TextAreaField(
        label="What's happening?", validators=[DataRequired(), Length(min=1, max=280)]
    )
    submit = SubmitField(label="Tweet")
