from api import models


def insert(db, userid, recipeid, rating):
    return models.insert(db, "ratings", {
        "userid": userid,
        "recipeid": recipeid,
        "rating": rating
    })


def delete(db, rowid):
    return models.delete(db, "ratings", rowid, "recipeid")


def select(db, rowid):
    return models.select(db, "ratings", {"rowid": rowid})


def from_recipe(db, recipeid):
    return models.query(db, "recipe_ratings", {"recipeid": recipeid})


def from_recipe_avg(db, recipeid):
    
    ratings, error = from_recipe(db, recipeid)
    if error:
        return models.error(error)

    values = tuple(map(lambda row: row["rating"], ratings))

    return None if len(values) == 0 else sum(values) / len(values)


def from_user(db, userid):
    return models.query(db, "user_ratings", {"userid": userid})


def dump(db):
    return models.dump(db, "ratings")
