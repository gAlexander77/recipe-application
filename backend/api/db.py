from flask import current_app as app
from flask import g

from api import models, db

import requests
import secrets
import sqlite3
import random
import os


def timestamp():
    from datetime import datetime
    return int(datetime.now().timestamp())


def sha3(string):
    from hashlib import sha3_256
    return sha3_256(string.encode("utf-8")).hexdigest()


def init(db_path, schema_path):
    database = sqlite3.connect(db_path)
    with open(schema_path) as stream:
        schema = stream.read()
    if len(schema) > 0:
        database.executescript(schema)
    database.close()


def load():
    if (db := getattr(g, "_database", None)) is None:
        db = g._database = sqlite3.connect(app.config.get("DB_PATH"))
        db.row_factory = lambda c, r: dict((c.description[i][0], v) for i, v in enumerate(r))
    return db


def close(execption):
    if (db := getattr(g, "_database", None)) is not None:
        db.close()


def demo(db_path, schema_path, uploads_dir, demo_dir):

    init(db_path, schema_path)

    def parse_recipes(path):
        
        with open(os.path.join(demo_dir, path), "rt") as stream:
            records = stream.read().split("\n\n\n")
        
        for record in records:
            items, recipe = record.split('\n'), {}
            for i, line in enumerate(items):
                if line.startswith("Recipe"):
                    recipe["name"] = items[i + 1]
                elif line.startswith("Image"):
                    url = items[i + 1]
                    name = sha3(recipe["name"]) + ".jpg"
                    path = os.path.join(uploads_dir, name)
                    if not os.path.isfile(path):
                        print(f"downloading: {name[:20]}...")
                        with requests.get(url) as response:
                            with open(path, "wb+") as stream:
                                stream.write(response.content)
                    recipe["image"] = path
                elif line.startswith("Description"):
                    recipe["description"] = items[i + 1]
                elif line.startswith("Instruction"):
                    l = 1
                    ins = ''
                    while not items[i + l].startswith("Ingredients"):
                        ins += items[i + l] + '\n'
                        l += 1
                    recipe["instructions"] = ins
                elif line.startswith("Ingredients"):
                    recipe["ingredients"] = []
                elif recipe.get("ingredients") is not None:
                    recipe["ingredients"].append(line)
            yield recipe

    def parse_users(path):
        with open(os.path.join(demo_dir, path)) as stream:
            return [line.strip().split(':') for line in stream.readlines()]

    def parse_comments(path):
        with open(os.path.join(demo_dir, path)) as stream:
            return [line.strip() for line in stream.readlines()]

    with app.app_context():

        database = db.load()
        comments = parse_comments("comments.txt")
        userids, recipeids = [], []

        for username, password in parse_users("users.txt"):
            print(f"+ adding user: {username} from users.txt")
            userids.append(models.users.insert(
                database, username, password))

        recipes = list(parse_recipes("recipes.txt"))
        random.shuffle(recipes)

        for recipe in recipes:
            print(f"+ adding recipe: {recipe['name'][:20]} from recipes.txt")
            recipeids.append(models.recipes.insert(
                database, random.choice(userids), 
                recipe["name"], recipe["ingredients"],
                recipe["description"], recipe["instructions"],
                recipe["image"]))

        staticids = recipeids.copy()

        for userid in userids:
            
            print(f"+ generating metadata for userid: {userid}")
            
            recipeids = staticids.copy()
            
            # generate ratings
            print("- + generating random ratings")
            for _ in range(random.randint(50, 77)):
                rating = float(random.randint(1, 5))
                recipeid = random.choice(recipeids)
                recipeids.remove(recipeid)
                models.ratings.insert(
                    database, userid, recipeid, rating)

            recipeids = staticids.copy()

            # generate comments
            print("- + selecting random comments from comments.txt")
            for _ in range(random.randint(15, 30)):
                comment = random.choice(comments)
                recipeid = random.choice(recipeids)
                recipeids.remove(recipeid)
                models.comments.insert(
                    database, userid, recipeid, comment)
