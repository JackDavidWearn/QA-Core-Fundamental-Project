CREATE TABLE IF NOT EXISTS films (
    films_id INTEGER NOT NULL AUTO_INCREMENT,
    films_title VARCHAR(250) NOT NULL,
    films_description VARCHAR(2000) NOT NULL,
    films_release INTEGER NOT NULL,
    films_time VARCHAR(6) NOT NULL,
    PRIMARY KEY (films_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS reviewer (
    reviewer_id INTEGER NOT NULL AUTO_INCREMENT,
    reviewer_name VARCHAR(250) NOT NULL,
    PRIMARY KEY (reviewer_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS review (
    review_id INTEGER NOT NULL AUTO_INCREMENT,
    fk_films_id INTEGER NOT NULL,
    fk_reviewer_id INTEGER NOT NULL,
    review_title VARCHAR(250) NOT NULL,
    review_body VARCHAR(2000) NOT NULL,
    review_stars INTEGER NOT NULL,
    PRIMARY KEY (films_id),
    FOREIGN KEY (fk_films_id) REFERENCES films(films_id),
    FOREIGN KEY (fk_reviewer_id) REFERENCES reviewer(reviewer_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;