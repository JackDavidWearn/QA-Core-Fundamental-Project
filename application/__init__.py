from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from os import getenv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = getenv('secret_key')

db = SQLAlchemy(app)

import application.routes