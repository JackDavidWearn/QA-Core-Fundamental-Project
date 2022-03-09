from flask_testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen
from flask import url_for

from application import app, db
from application.models import Films
from application.forms import AddFilm

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
        self.driver.get(f'http://localhost:5050/create-film')

    def tearDown(self):
        self.driver.quit()
        db.drop_all()
    
    def test_server_running(self):
        response = urlopen('http://localhost:5050/create-film')
        self.assertEqual(response.code, 200)

class TestAddFilm(TestBase):
    TEST_CASES = ('Film 1', 'Desc for film 1', 2022, '1h1m'), ('Film 2', 'Desc for film 2', 2021, '2h1m')

    def submit_input(self, case):
        self.driver.find_element_by_xpath('/html/body/div[2]/div/form/input[2]').send_keys(case[0])
        self.driver.find_element_by_xpath('/html/body/div[2]/div/form/input[3]').send_keys(case[1])
        self.driver.find_element_by_xpath('/html/body/div[2]/div/form/input[4]').send_keys(case[2])
        self.driver.find_element_by_xpath('/html/body/div[2]/div/form/input[5]').send_keys(case[3])
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

    def test_add_film(self):
        for case in self.TEST_CASES:
            self.submit_input(case)
            films = Films.query.filter_by(films_title=case[0]).all()
            self.assertNotEqual(films, None)