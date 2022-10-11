#!/usr/bin/env python3
import sys; sys.path.append("./src")
import sql
import os

from random import randint, choice, random, shuffle
from base64 import b64decode

UNITS = ["oz", "lbs", "floz", "tbsp", "tsp"]

# import a file as an array of lines
def load_file(path):
    with open(path, "rt+") as file:
        return [line.strip() for line in file.readlines()]


def gen_usernames(a, b):
    names = load_file("./docs/testing/names.txt")
    shuffle(names)
    return [name.lower() for name in names[:randint(a, b)]]


def gen_recipe_pairs(a, b):
    recipes = load_file("./docs/testing/recipes.txt")
    shuffle(recipes)
    for line in recipes[:randint(a, b)]:
        title, encoded_description = line.split(':')
        yield title, b64decode(encoded_description.encode("utf-8")).decode("utf-8")


def gen_ingredient_names(a, b):
    names = load_file("./docs/testing/ingredients.txt")
    shuffle(names)
    return names[:randint(a, b)]


def gen_users(db, limit=15):
    for username in gen_usernames(5, limit):
        id, error = sql.insert.user(db, username, "ravioli")
        if error:
            print(f"error inserting {username}:", error)
        else:
            yield id, username


def gen_recipes(db, user, limit=5):
    for title, description in gen_recipe_pairs(1, limit):
        id, error = sql.insert.recipe(db, user, title, description)
        if error:
            print(f"error inserting {title}:", error)
        else:
            yield id, title


def gen_ingredients(db, recipe, limit=7):
    for name in gen_ingredient_names(3, limit):
        ingredient, error = sql.select.ingredient(db, name=name)
        if not ingredient:
            id, error = sql.insert.ingredient(db, name)
            if error:
                print(error, "continuing")
                continue
        else:
            id = ingredient[0]
        _, error = sql.insert.recipe_ingredient(db, recipe, id, choice(UNITS), 2 + (random() * 24))
        if error:
            print(error)
        else:
            yield id, name


if __name__ == "__main__":
    
    if os.path.isfile(sql.DATABASE_PATH):
        input(f"""this will delete the current database located at {sql.DATABASE_PATH}
                press [ENTER] to continue
                press [CTRL+C] to abort > """)
        os.remove(sql.DATABASE_PATH)

    db = sql.open_database()

    user_ids, recipe_ids = [], []

    for user_id, username in gen_users(db):
        print(user_id, username)
        user_ids.append(user_id)
        for recipe_id, title in gen_recipes(db, user_id):
            print("-", recipe_id, title)
            recipe_ids.append(recipe_id)
            for ingredient_id, name in gen_ingredients(db, recipe_id):
                print("--", ingredient_id, name)

    for _ in range(randint(25, 30)):
        uid = choice(user_ids)
        rid = choice(recipe_ids)
        pinned = True if random() > 0.5 else False
        rating = randint(0, 5)
        print(f"user[{uid[:5]}...] rates recipe[{rid[:5]}...] {rating}/5 stars")
        if pinned:
            print("  and saves the recipe")
        _, error = sql.insert.user_recipe(db, uid, rid, rating, pinned)
        if error:
            print(error)

    db.close()
