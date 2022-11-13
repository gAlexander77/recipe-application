from api import models


def insert(db, userid, name, description, instructions, image):
    return models.insert(db, "recipes", {
        "userid": userid,
        "name": name,
        "description": description,
        "instructions": instructions,
        "image": image
    })


def delete(db, rowid):
    return models.delete(db, "recipes", rowid, "name")


def select(db, rowid):
    return models.select(db, "recipes", {"rowid": rowid})


def query(db, userid):
    return models.query(db, "recipes", {"userid": userid})


def dump(db):
    return models.dump(db, "recipes")


def ratings_avg(db, rowid):
    ratings, e = models.ratings.from_recipe(db, recipeid=rowid)
    if e:
        return models.error(e)

    values = tuple(map(lambda row: row["rating"], ratings))

    return None if len(values) == 0 else sum(values) / len(values)
