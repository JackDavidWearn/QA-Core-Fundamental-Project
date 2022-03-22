from flask import redirect, url_for, render_template, request
from application import app, db
from application.models import Films, Reviewer, Review
from application.forms import AddFilm, AddReviewer, AddReview

# Home route, to display the home page
@app.route('/')
@app.route('/home')
def home():
    num_films = Films.query.count()
    films = Films.query.all()
    reviews = Review.query.all()
    reviewers = Reviewer.query.all()
    return render_template('index.html', num=num_films, films=films, reviews=reviews, reviewers=reviewers, pageTitle="Home")

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
    return render_template('add_reviewer.html', form=form, pageTitle="Add Reviewer")

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
    return render_template('add_film.html', form=form, pageTitle="Add Film")

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
    return render_template('add_review.html', form=form, pageTitle="Add Review")

# View all movies route
@app.route('/view-all-films', methods=['GET', 'POST'])
def viewallfilms():
    num_films = Films.query.count()
    films = Films.query.all()
    return render_template('view_all_films.html', num_films=num_films, films=films, pageTitle="All Films")

# View all reviews for a specific movie
@app.route('/view-film-reviews/<int:films_id>', methods=['GET', 'POST'])
def viewfilmreviews(films_id):
    film = Films.query.get(films_id)
    films = Films.query.all()
    reviews = Review.query.all()
    reviewers = Reviewer.query.all()
    return render_template('specific_film_review.html', films=films, film=film, reviews=reviews, reviewers=reviewers, pageTitle="Reviews")

# View all reviewers route
@app.route('/view-all-reviewers', methods=['GET', 'POST'])
def viewallreviewers():
    num_reviewers = Reviewer.query.count()
    reviewers = Reviewer.query.all()
    return render_template('view_all_reviewers.html', num_reviewers=num_reviewers, reviewers=reviewers, pageTitle="All Reviewers")

# View all reviews route
@app.route('/view-all-reviews', methods=['GET', 'POST'])
def viewallreviews():
    num_reviews = Review.query.count()
    reviews = Review.query.all()
    return render_template('view_all_reviews.html', num_reviews=num_reviews, reviews=reviews, pageTitle="All Reviews")

# Update a movie route
@app.route('/update-film/<int:films_id>', methods=['GET', 'POST'])
def updatefilm(films_id):
    film = Films.query.get(films_id)
    form = AddFilm()
    if request.method == 'POST':
        film.films_title = form.films_title.data
        film.films_description = form.films_description.data
        film.films_release = form.films_release.data
        film.films_time = form.films_time.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_film.html', form=form, pageTitle="Update Film")

# Update a reviewer route
@app.route('/update-reviewer/<int:reviewer_id>', methods=['GET', 'POST'])
def updatereviewer(reviewer_id):
    reviewer = Reviewer.query.get(reviewer_id)
    form = AddReviewer()
    if request.method == 'POST':
        reviewer.reviewer_name = form.reviewer_name.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_reviewer.html', form=form, pageTitle="Update Reviewer")

# Update a review route
@app.route('/update-review/<int:review_id>', methods=['GET', 'POST'])
def updatereview(review_id):
    film = Films.query.all()
    reviewer = Reviewer.query.all()
    review = Review.query.get(review_id)
    form = AddReview()
    form.films.choices.extend([(film.films_id, str(film)) for film in film])
    form.reviewers.choices.extend([(reviewer.reviewer_id, str(reviewer)) for reviewer in reviewer])
    if request.method == 'POST':
        review.film = form.films.data
        review.reviewer = form.reviewers.data
        review.title = form.review_title.data
        review.body = form.review_body.data
        review.stars = form.review_stars.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_review.html', form=form, pageTitle="Update Review")


# Delete a movie route
@app.route('/delete-film/<int:films_id>')
def deletefilm(films_id):
    film = Films.query.get(films_id)
    db.session.delete(film)
    db.session.commit()
    return redirect(url_for('home'))

# Delete a reviewer route
@app.route('/delete-reviewer/<int:reviewer_id>')
def deletereviewer(reviewer_id):
    reviewer = Reviewer.query.get(reviewer_id)
    db.session.delete(reviewer)
    db.session.commit()
    return redirect(url_for('home'))

# Delete a review route
@app.route('/delete-review/<int:review_id>')
def deletereview(review_id):
    review = Review.query.get(review_id)
    db.session.delete(review)
    db.session.commit()
    return redirect(url_for('home'))