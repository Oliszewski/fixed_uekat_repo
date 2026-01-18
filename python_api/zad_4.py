from fastapi import FastAPI
import csv

app = FastAPI()


class Movie:
    def __init__(self, movieId, title, genres):
        self.movieId = movieId
        self.title = title
        self.genres = genres


class Link:
    def __init__(self, movieId, imdbId, tmdbId):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId


class Rating:
    def __init__(self, userId, movieId, rating, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp


class Tag:
    def __init__(self, userId, movieId, tag, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp


def get_csv_data(filename, class_model):
    data_list = []
    try:
        with open(filename, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:

                obj = class_model(**row)
                data_list.append(obj.__dict__)
    except FileNotFoundError:
        return [{"error": f"Nie znaleziono pliku {filename}"}]
    return data_list


@app.get("/movies")
def get_movies():
    return get_csv_data("movies.csv", Movie)


@app.get("/links")
def get_links():
    return get_csv_data("links.csv", Link)


@app.get("/ratings")
def get_ratings():
    return get_csv_data("ratings.csv", Rating)


@app.get("/tags")
def get_tags():
    return get_csv_data("tags.csv", Tag)
