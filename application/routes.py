from crypt import methods
from flask import redirect, url_for, render_template, request
from application import app, db
from application.models import Films, Reviewer
from application.forms import AddFilm, AddReviewer

# Home route, to display the home page
@app.route('/')
def home():
    num_films = Films.query.count()
    films = Films.query.all()
    return render_template('index.html', num=num_films, films=films)

# Create a reviewer route
@app.route('/create-reviewer', methods=['GET', 'POST'])
def createreviewer():
    form = AddReviewer()
    if request.method == "POST":
        name = form.reviewer_name.data
        new_reviewer = Reviewer(reviewer_name=name)
        db.session.add(new_reviewer)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_reviewer.html')

# Create a film route
@app.route('/create-film', methods=['GET', 'POST'])
def createfilm():
    form = AddFilm()
    if request.method == "POST":
        title = form.films_title.data
        description = form.films_description.data
        release = form.films_release.data
        time = form.films_time.data
        new_film = Films(films_title=title, films_description=description, films_release=release, films_time=time)
        db.session.add(new_film)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_film.html')

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