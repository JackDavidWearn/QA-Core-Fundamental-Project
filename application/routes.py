from flask import redirect, url_for, render_template, request
from application import app, db
from application.models import Films, Reviewer, Review
from application.forms import AddFilm, AddReviewer, AddReview

# Home route, to display the home page
@app.route('/')
def home():
    num_films = Films.query.count()
    films = Films.query.all()
    reviews = Review.query.all()
    return render_template('index.html', num=num_films, films=films, reviews=reviews)

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
    return render_template('add_reviewer.html', form=form)

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
    return render_template('add_film.html', form=form)

# Create a review route
@app.route('/create-review', methods=['GET', 'POST'])
def createreview():
    film = Films.query.all()
    reviewer = Reviewer.query.all()
    form = AddReview()
    form.films.choices.extend([(film.films_id, str(film)) for film in film])
    form.reviewers.choices.extend([(reviewer.reviewer_id, str(reviewer)) for reviewer in reviewer])
    if request.method == "POST":
        film = form.films.data
        reviewer = form.reviewers.data
        title = form.review_title.data
        body = form.review_body.data
        stars = form.review_stars.data
        new_review = Review(fk_films_id=film, fk_reviewer_id=reviewer, review_title=title, review_body=body, review_stars=stars)
        db.session.add(new_review)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_review.html', form=form)
