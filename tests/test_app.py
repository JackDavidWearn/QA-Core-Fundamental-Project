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
        sample_reviewer = Reviewer(reviewer_name="Sample reviewer")
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
            data = dict(reviewer_name="Sample reviewer"),
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

class TestViewAllFilms(TestBase):
    def test_view_get(self):
        response = self.client.get(url_for('viewallfilms'))
        self.assert200(response)
        self.assertIn(b'Sample Film', response.data)

class TestViewSpecificFilms(TestBase):
    def test_view_get(self):
        response = self.client.get(url_for('viewfilmreviews', films_id=1))
        self.assert200(response)

class TestViewAllReviewers(TestBase):
    def test_view_get(self):
        response = self.client.get(url_for('viewallreviewers'))
        self.assert200(response)
        self.assertIn(b'Sample reviewer', response.data)

class TestViewAllReviews(TestBase):
    def test_view_get(self):
        response = self.client.get(url_for('viewallreviews'))
        self.assert200(response)
        self.assertIn(b'Sample Review', response.data)

class TestUpdateFilm(TestBase):
    def test_get(self):
        response = self.client.get(url_for('updatefilm', films_id=1))
        self.assert200(response)

    def test_update_film(self):
        response = self.client.post(
            url_for('updatefilm', films_id=1),
            data = dict(films_title="Updated Title", films_description="Updated Description", films_release=2021, films_time="Test"),
            follow_redirects=True
        )
        self.assertIn(b'home', response.data)
        self.assert200(response)

class TestUpdateReviewer(TestBase):
    def test_get(self):
        response = self.client.get(url_for('updatereviewer', reviewer_id=1))
        self.assert200(response)


    def test_update_reviewer(self):
        response = self.client.post(
            url_for('updatereviewer', reviewer_id=1),
            data = dict(reviewer_name="Updated Reviewer"),
            follow_redirects=True
        )
        self.assertIn(b'home', response.data)

class TestUpdateReview(TestBase):
    def test_get(self):
        response = self.client.get(url_for('updatereview', review_id=1))
        self.assert200(response)

    def test_update_review(self):
        response = self.client.post(
            url_for('updatereview', review_id=1),
            data = dict(fk_films_id=1, fk_reviewer_id=1, review_title="Updated Review", review_body="Updated Review", review_stars="1"),
            follow_redirects=True
        )
        self.assertIn(b'home', response.data)

class TestDeleteFilm(TestBase):
    def test_delete_film(self):
        response = self.client.get(url_for('deletefilm', films_id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'home', response.data)
        self.assertNotIn(b'Sample Film', response.data)

class TestDeleteReviewer(TestBase):
    def test_delete_reviewer(self):
        response = self.client.get(url_for('deletereviewer', reviewer_id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'home', response.data)
        self.assertNotIn(b'Sample Reviewer', response.data)

class TestDeleteReview(TestBase):
    def test_delete_review(self):
        response = self.client.get(url_for('deletereview', review_id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'home', response.data)
        self.assertNotIn(b'Sample Review', response.data)