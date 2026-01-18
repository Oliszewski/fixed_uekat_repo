from fastapi import FastAPI
import csv

app = FastAPI()


class Movie:
    def __init__(self, movieId, title, genres):
        self.movieId = movieId
        self.title = title
        self.genres = genres


@app.get("/movies")
def get_movies():
    results = []

    with open("movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:

            movie = Movie(**row)

            results.append(movie.__dict__)

    return results
