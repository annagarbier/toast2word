from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class GuessForm(FlaskForm):
    guess = StringField("Guess", validators=[
                        DataRequired()], render_kw={'autofocus': True})
    submit = SubmitField("Submit")


class StartForm(FlaskForm):
    submit = SubmitField("Play!")
