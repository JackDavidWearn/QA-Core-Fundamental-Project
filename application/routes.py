from flask import redirect, url_for, render_template, request
from application import app, db
from application.models import Films, Reviewer

# Home route, to display the home page
@app.route('/')
def home():
    return Films.data()

# Create a reviewer route
@app.route('/create-reviewer')
def createreviewer():
    return redirect(url_for('home'))