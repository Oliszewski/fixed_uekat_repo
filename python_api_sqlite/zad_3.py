from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from zad_1 import Movie, Link, Rating, Tag

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Witaj w API MovieLens!"}


@app.get("/movies")
def get_movies(db: Session = Depends(get_db)):
    return db.query(Movie).all()


@app.get("/links")
def get_links(db: Session = Depends(get_db)):
    return db.query(Link).all()


@app.get("/ratings")
def get_ratings(db: Session = Depends(get_db)):

    return db.query(Rating).limit(100).all()


@app.get("/tags")
def get_tags(db: Session = Depends(get_db)):
    return db.query(Tag).all()
