from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired
from datetime import date
from application.models import Films, Reviewer, Review

class AddFilm(FlaskForm):
    films_title = StringField("Film Title", validators=[DataRequired()])
    films_description = StringField("Description of film", validators=[DataRequired()])
    films_release = IntegerField("Year of release", validators=[DataRequired()])
    films_time = StringField("Runtime of move in form XXhYYM", validators=[DataRequired()])
    submit = SubmitField("Add film to database")

class AddReviewer(FlaskForm):
    reviewer_name = StringField("Enter your name", validators=[DataRequired()])
    submit = SubmitField("Add Reveiwer")

class AddReview(FlaskForm):
    films = SelectField("Film you wish to review", choices=[])
    reviewers = SelectField("Who is making the review?", choices=[])
    review_title = StringField("Enter the title for your review", validators=[DataRequired()])
    review_body = StringField("Enter your review", validators=[DataRequired()])
    review_stars = IntegerField("How many stars out of 5 would you give it?", validators=[DataRequired()])
    submit = SubmitField("Add Review")
