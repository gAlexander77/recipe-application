from api import models


def insert(db, userid, recipeid, rating):
    return models.insert(db, "ratings", {
        "userid": userid,
        "recipeid": recipeid,
        "rating": rating
    })


def delete(db, id):
    return models.delete(db, "ratings", id, "rating")


def avg(db, recipeid):
    row = models.select_one(db, "avg_ratings", columns="rating", filters={
        "recipeid": recipeid
    })
    return row["rating"] if row is not None else 0
