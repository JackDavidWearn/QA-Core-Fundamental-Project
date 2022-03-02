from application import db

class Films(db.Model):
    films_id = db.Column(db.Intger, primary_key=True)
    films_title = db.Column(db.String(250))
    films_description = db.Column(db.String(2000))
    films_release = db.Column(db.Date)
    films_time = db.Column(db.String(6))

    def __str__(self):
        return f"Film Title: {self.films_title}\n Film Description: {self.films_description}\n Film Release Date: {self.films_release}\n Film Running Time: {self.films_time}"
