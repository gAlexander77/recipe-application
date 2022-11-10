from api import models

def dump(db):

    recipes, error = models.dump(db, "recipe_cards")
    if error:
        return models.error(error)

    for recipe in recipes:

        recipe["comments"] = models.recipes.comment_count(db, recipe["rowid"])
        recipe["user"] = {
            "rowid": recipe["userid"],
            "username": recipe["username"]
        }

        del recipe["userid"]
        del recipe["username"]
    
    return models.ok(recipes)
