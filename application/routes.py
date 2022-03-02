from flask import redirect, url_for, render_template, request
from application import app, db
from application.models import Films, Reviewer

# Home route, to display the home page
@app.route('/')
def home():
    return render_template('index.html')

# Create a reviewer route
@app.route('/create-reviewer')
def createreviewer():
    return redirect(url_for('home'))

# Create a film route
@app.route('/create-film')
def createfilm():
    return redirect(url_for('home'))

# Update a reviewer route
@app.route('/update-reviewer/<int:reviewer_id>')
def updatereviewer(reviewer_id):
    return redirect(url_for('home'))

# Update a film route
@app.route('/update-film/<int:films_id>')
def updatefilm(films_id):
    return redirect(url_for('home'))

# Delete a reviewer route
@app.route('/delete-reviewer/<int:reviewer_id>')
def deletereviewer(reviewer_id):
    return redirect(url_for('home'))

# Delete a film route
@app.route('/delete-film/<int:films_id>')
def deletefilm(films_id):
    return redirect(url_for('home'))