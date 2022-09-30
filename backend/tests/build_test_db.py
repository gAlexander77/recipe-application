#!/usr/bin/env python3

import string
import random
import sys
import os

if not os.path.isdir("./src"):
    print("must be in 'backend/' directory")
    exit(0)
sys.path.append("./src")

import sql

TEST_PATH = "./documents/testing"

def gibberish() -> str:
    words = []
    for _ in range(random.randint(20, 120)):
        word = ''
        for _ in range(random.randint(1, 12)):
            word += random.choice(string.ascii_letters)
        words.append(word)
    return ' '.join(words)

def load_list(path: str) -> list:
    with open(path, "rt") as file:
        return [line.strip() for line in file.readlines()]

if __name__ == "__main__":
    
    db = sql.load_database()
    names = load_list(f"{TEST_PATH}/names.txt")
    foods = load_list(f"{TEST_PATH}/ingredients.txt")
    units = load_list(f"{TEST_PATH}/units.txt")

    for _ in range(random.randint(5, 50)):
        username = random.choice(names) + '_%04d' % random.randint(0, 9999)
        ok, uuid = sql.insert_user(db, username, "password")
        if not ok:
            print(f"error inserting {username}")
            db.close()
            exit()
        print(f"inserted user {username}")
        for i in range(random.randint(0, 10)):
            recipe = f"{username} Recipe {i + 1}"
            print(f"generating ingredients for {recipe}")
            ingredients = {}
            for _ in range(random.randint(2, 12)):
                ingredients[random.choice(foods)] = [random.choice(units), random.random() * 20]
                print(f"> ingredient genereated")
            ok, _ = sql.insert_recipe(db, uuid, recipe, gibberish(), ingredients)
            if not ok:
                print(f"error inserting recipe: {recipe} {ingredients}")
                db.close()
                exit()
    print("test database generated!")
    db.close()
