from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired
from datetime import date
from application.models import Films, Reviewer

class AddFilm(FlaskForm):
    films_title = StringField("Film Title", validators=[DataRequired()])
    films_description = StringField("Description of film", validators=[DataRequired()])
    films_release = IntegerField("Year of release", validators=[DataRequired()])
    films_time = StringField("Runtime of move in form XXhYYM", validators=[DataRequired()])
    submit = SubmitField("Add film to database")

class AddReviewer(FlaskForm):
    reviewer_name = StringField("Enter your name", validators=[DataRequired()])

