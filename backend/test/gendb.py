#!/usr/bin/env python3
import sys; sys.path.append("./src")
import sql
import os

from random import randint, choice, random, shuffle
from base64 import b64decode

PASSWORD = "ravioli"
TSIZE = os.get_terminal_size().columns + 18
UNITS = ["oz", "lbs", "floz", "tbsp", "tsp"]
CLS = f"\033[2K\033[{TSIZE}D"

def output(text, newline=False):
    fulltext = CLS + text
    print(fulltext[:TSIZE], flush=True, end='\n' if newline else '')


# import a file as an array of lines
def load_file(path):
    with open(path, "rt+") as file:
        return [line.strip() for line in file.readlines()]


def gen_usernames(a, b):
    names = load_file("./docs/testing/names.txt")
    shuffle(names)
    return [name.lower() + str(randint(0, 9999)) for name in names[:randint(a, b)]]


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


def gen_users(db, limit=25):
    for username in gen_usernames(5, limit):
        id, error = sql.insert.user(db, username, PASSWORD)
        if error:
            print(f"error inserting {username}:", error)
        else:
            yield id, username


def gen_recipes(db, user, limit=7):
    for title, description in gen_recipe_pairs(1, limit):
        id, error = sql.insert.recipe(db, user, title, description)
        if error:
            print(f"error inserting {title}:", error)
        else:
            yield id, title


def gen_ingredients(db, recipe, limit=10):
    for name in gen_ingredient_names(3, limit):
        ingredient, error = sql.select.ingredient(db, name=name)
        if not ingredient:
            id, error = sql.insert.ingredient(db, name)
            if error is not None:
                continue
        else:
            id = ingredient[0]
        _, error = sql.insert.recipe_ingredient(db, recipe, id, choice(UNITS), 2 + (random() * 24))
        if error is not None:
            print(error)
        else:
            yield id, name


if __name__ == "__main__":
    
    if os.path.isfile(sql.DATABASE_PATH):
        try:
            input(f"""this will delete the current database located at {sql.DATABASE_PATH}
press [\033[32mENTER\033[0m] to continue
press [\033[33mCTRL+C\033[0m] to abort > """)
        except KeyboardInterrupt:
            exit(0)
        os.remove(sql.DATABASE_PATH)

    db = sql.open_database()
    
    user_limit, recipe_limit, ingredient_limit = 20, 12, 15
    user_ids, recipe_ids = [], []

    for user_id, username in gen_users(db, user_limit):
        output(f"user \033[36m{username}\033[0m created with ID \033[32m{user_id[:10]}\033[0m...", newline=True)
        user_ids.append(user_id)
        for recipe_id, title in gen_recipes(db, user_id, recipe_limit):
            recipe_ids.append(recipe_id)
            icount = 0
            for i, (ingredient_id, name) in enumerate(gen_ingredients(db, recipe_id, ingredient_limit)):
                output(f"    \033[34m>\033[0m `{name}` {ingredient_id}")
                icount = i
            output(f"  \033[33m-\033[0m `{title}` recipe created with [\033[36m{icount}\033[0m] ingredients", newline=True)

    for _ in range(randint(150, 200)):
        uid = choice(user_ids)
        rid = choice(recipe_ids)
        pinned = True if random() > 0.5 else False
        rating = randint(0, 5)
        output(f"{uid[:20]}... rates {rid[:20]}... {rating}/5 stars")
        if pinned:
            output(f"{uid[:20]}... pinned {rid[:20]}...")
        _, error = sql.insert.user_recipe(db, uid, rid, rating, pinned)
        if error:
            output(error, newline=True)

    output(f"all user passwords: \033[31m{PASSWORD}\033[0m", newline=True)
    output("\033[32m+\033[0m sample database generated", newline=True)

    db.close()
