#!/usr/bin/env python3

import string
import random
import sys
import os

sys.path.append("./src")
import sql

TEST_PATH = "./docs/testing"

def gibberish(n, m) -> str:
    words = []
    for _ in range(random.randint(1, n)):
        word = ''
        for _ in range(random.randint(3, m)):
            word += random.choice(string.ascii_letters)
        words.append(word)
    return ' '.join(words)

def load_list(path: str) -> list:
    with open(path, "rt") as file:
        return [line.strip() for line in file.readlines()]

if __name__ == "__main__":
    
    db = sql.open_database()
    names = load_list(f"{TEST_PATH}/names.txt")
    foods = load_list(f"{TEST_PATH}/ingredients.txt")
    units = load_list(f"{TEST_PATH}/units.txt")

    for entry in range(random.randint(5, 50)):
        username = random.choice(names) + '_%04d' % random.randint(0, 9999)
        uuid, error = sql.insert.user(db, username, "password")
        if error:
            print(f"error inserting {username}: {error}")
            db.close()
            exit()
        print(f"inserted user #{entry} {username}")
        for i in range(random.randint(0, 10)):
            recipe = gibberish(4, 6)
            print(f"generating ingredients for {recipe}")

            rid, error = sql.insert.recipe(db, uuid, recipe, gibberish(30, 10), random.randint(0, 10))
            if error:
                print(f"error inserting {recipe}: {error}")
                db.close()
                exit()
            
            for _ in range(random.randint(2, 12)):
                ingredient = random.choice(foods) 
                unit = random.choice(units)
                count = random.random() * 20
                iid, error = sql.insert.ingredient(db, ingredient)
                if error:
                    sql.insert.recipe_ingredient(db, rid, iid, unit, count)
                print(f"> ingredient genereated")
    print("test database generated!")
    db.close()
