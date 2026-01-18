import csv
from database import SessionLocal
from zad_1 import Movie, Link, Rating, Tag


def load_csv(filename, model_class):
    db = SessionLocal()
    try:

        if db.query(model_class).first():
            print(f"{model_class.__tablename__}")
            return

        print(f"Ładowanie pliku {filename}...")
        with open(filename, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            batch = []
            for row in reader:

                if "tmdbId" in row and row["tmdbId"] == "":
                    row["tmdbId"] = None

                obj = model_class(**row)
                batch.append(obj)

            db.add_all(batch)
            db.commit()
            print(f"{model_class.__tablename__}")

    except FileNotFoundError:
        print(f"There is no such a file!{filename}.")
    except Exception as e:
        print(f"ERROR {filename}: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    load_csv("movies.csv", Movie)
    load_csv("links.csv", Link)
    load_csv("ratings.csv", Rating)
    load_csv("tags.csv", Tag)
