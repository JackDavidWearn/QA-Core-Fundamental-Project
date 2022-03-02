from sqlalchemy import ForeignKey
from application import db

class Films(db.Model):
    films_id = db.Column(db.Integer, primary_key=True)
    films_title = db.Column(db.String(250))
    films_description = db.Column(db.String(2000))
    films_release = db.Column(db.Integer)
    films_time = db.Column(db.String(6))
    fk_reviewers_id = db.Column(db.Integer, db.ForeignKey('reviewer.reviewer_id'))

    def __str__(self):
        return f"Film Title: {self.films_title}\n Film Description: {self.films_description}\n Film Release Date: {self.films_release}\n Film Running Time: {self.films_time}"

class Reviewer(db.Model):
    reviewer_id = db.Column(db.Integer, primary_key=True)
    reviewer_name = db.Column(db.String(250))

    def __str__(self):
        return f"{self.reviewer_name}"

class Review(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    fk_films_id = db.Column(db.Integer, ForeignKey('films.films_id'))
    fk_reviewer_id = db.Column(db.Integer, ForeignKey('reviewer.reviewer_id'))
    review_title = db.Column(db.String(250))
    review_body = db.Column(db.String(2000))
    review_stars = db.Column(db.Integer)

    def __str__(self):
        return f"Reviewer: {self.fk_reviewer_id} reviewed: {self.fk_films_id}. Title: {self.review_title} || Body: {self.review_body} || Stars: {self.review_stars}"
