from sqlalchemy import Column, Integer, String, Float
from database import Base, engine


class Movie(Base):
    __tablename__ = "movies"

    movieId = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    genres = Column(String)


class Link(Base):
    __tablename__ = "links"
    movieId = Column(Integer, primary_key=True)
    imdbId = Column(String)
    tmdbId = Column(String)


class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer)
    movieId = Column(Integer)
    rating = Column(Float)
    timestamp = Column(Integer)


class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer)
    movieId = Column(Integer)
    tag = Column(String)
    timestamp = Column(Integer)


if __name__ == "__main__":
    print("Tworzenie tabel w bazie danych...")
    Base.metadata.create_all(bind=engine)
    print("Gotowe! Utworzono plik sql_app.db")
