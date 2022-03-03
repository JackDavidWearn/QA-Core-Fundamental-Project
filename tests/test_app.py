from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Films, Reviewer, Review
from datetime import date, timedelta

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
            SECRET_KEY = 'testsecretkey',
            DEBUG_MODE = True,
            WTF_CSRF_ENABLED = False
        )
        return app
    
    def setUp(self):
        db.create_all()
        sample_film = Films(films_title="Sample Film", films_description="Sample Description for sample films", films_release=2022, films_time="10h59m")
        sample_reviewer = Reviewer(reviewer_name="Sample Name")
        sample_review = Review(fk_films_id=1, fk_reviewer_id=1, review_title="Sample Review", review_body="Sample Review Body", review_stars=5)
        db.session.add(sample_film)
        db.session.add(sample_reviewer)
        db.session.add(sample_review)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestHome(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)
        self.assertIn(b'Sample Film', response.data)


class TestAddFilm(TestBase):
    def test_create_get(self):
        response = self.client.get(url_for('createfilm'))
        self.assert200(response)
    
    def test_create_post(self):
        response = self.client.post(
            url_for('createfilm'),
            data = dict(films_title="Sample Film", films_description="Sample Description for sample films", films_release=2022, films_time="10h59m"), 
            follow_redirects = True
        )
        self.assert200(response)

class TestAddReviewer(TestBase):
    def test_create_get(self):
        response = self.client.get(url_for('createreviewer'))
        self.assert200(response)

    def test_create_post(self):
        response = self.client.post(
            url_for('createreviewer'),
            data = dict(reviewer_name="Sample Name"),
            follow_redirects = True
        )
        self.assert200(response)

class TestAddReview(TestBase):
    def test_create_get(self):
        response = self.client.get(url_for('createreview'))
        self.assert200(response)

    def test_create_post(self):
        response = self.client.post(
            url_for('createreview'),
            data = dict(fk_films_id=1, fk_reviewer_id=1, review_title="Sample Review", review_body="Sample Review Body", review_stars=5),
            follow_redirects = True
        )
        self.assert200(response)