#!/usr/bin/env python3

import sqlite3

from xml.etree.ElementTree import parse
from base64 import b64encode
from sys import argv


if __name__ == "__main__":

    if len(argv) != 2:
        print("supply the xml file")
        exit(0)

    tree = parse(argv[1])
    root = tree.getroot()

    with open("recipes.txt", "wt+") as file:
        for recipe in root.iter("recipe"):
            name = recipe.attrib["description"]
            description = list(recipe.iter("XML_MEMO1"))[0].text
            print(name, b64encode(description.encode("utf-8")).decode("utf-8"), sep=':', file=file)

    with open("ingredients.txt", "wt+") as file:
        ingredients = set()
        for ingredient in root.iter("ingredient"):
            ingredients.add(ingredient.attrib["description"])
        for ingredient in ingredients:
            print(ingredient, file=file)
