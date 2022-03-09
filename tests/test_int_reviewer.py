from flask_testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen
from flask import url_for

from application import app, db
from application.models import Reviewer
from application.forms import AddReviewer

class TestBase(LiveServerTestCase):
    def create_app(self):
        app.config.update(
            SQLALCHAMEY_DATABASE_URI = 'sqlite:///test.db',
            LIVESERVER_PORT = 5050,
            DEBUG = True,
            TESTING = True
        )
        return app

    def setUp(self):
        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options = chrome_options)
        db.create_all()
        self.driver.get(f'http://localhost:5050/create-reviewer')

    def tearDown(self):
        self.driver.quit()
        db.drop_all()
    
    def test_server_running(self):
        response = urlopen('http://localhost:5050/create-reviewer')
        self.assertEqual(response.code, 200)

class TestAddFilm(TestBase):
    TEST_CASES = ('Reviewer 1'), ('Reviewer 2')

    def submit_input(self, case):
        
        self.driver.find_element_by_xpath('/html/body/div[2]/div/form/input[2]').send_keys(case[0])
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

    def test_add_reviewer(self):
        for case in self.TEST_CASES:
            self.submit_input(case)
            reviewers = Reviewer.query.filter_by(reviewer_name=case[0]).all()
            self.assertNotEqual(reviewers, None)