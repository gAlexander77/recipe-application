from api import models

def dump(db):

    recipes, error = models.dump(db, "recipe_cards")
    if error:
        return models.error(error)

    for recipe in recipes:

        rowid = recipe["rowid"]

        comments, e = models.comments.from_recipe(db, rowid)
        if e:
            return error(e)

        recipe["comments"] = len(comments)
        recipe["rating"] = models.recipes.ratings_avg(db, rowid)
        recipe["user"] = {
            "rowid": recipe["userid"],
            "username": recipe["username"]
        }

        del recipe["userid"]
        del recipe["username"]
    
    return models.ok(recipes)
