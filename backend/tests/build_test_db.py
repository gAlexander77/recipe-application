#!/usr/bin/env python3

import random
import sys
import os

if not os.path.isdir("./src"):
    print("must be in 'backend/' directory")
    exit(0)
sys.path.append("./src")

import sql

NAMES = "./documents/testing"

def load_names(path: str):
    with open(path, "rt") as file:
        return [line.strip() for line in file.readlines()]

if __name__ == "__main__":
    
    db = sql.load_database()
    names = load_names(f"{NAMES}/names.txt")

    for _ in range(50):
        username = random.choice(names) + '_%03d' % random.randint(0, 999)
        sql.insert_user(db, username, "password")

    db.close()
