#!/usr/bin/env python3

from getpass import getpass

import requests
import sys
import os


def build_url(address, path):
    return f"http://{address}/api/{path}"


def login(address, username, password):
    session = requests.session()
    user = { "username": username, "password": password }
    url = build_url(address, "auth/login")
    with session.post(url, json=user) as response:
        try:
            data = response.json()
            if not data["ok"]:
                print(data["error"])
            else:
                return session
        except:
            print(response.text)


def logout(address, session):
    url = build_url(address, "auth/logout")
    with session.post(url) as response:
        return response.json()["ok"]


def input_ingredients():
    return [input(f"> ingredient {i}: ") for i in range(int(input("how many ingredients?: ")))]


def all_recipes(session, address):
    url = build_url(address, "recipes/")
    with session.get(url) as response:
        data = response.json()
        return data.get("data"), data.get("error")


def get_recipe(session, address, rowid):
    url = build_url(address, f"recipes/{rowid}")
    with session.get(url) as response:
        data = response.json()
        return data.get("data"), data.get("error")


def create_recipe(session, address, name=None, ingredients=None, description=None, instructions=None):
    url = build_url(address, "recipes/create")
    recipe = { "name": input("name: ") if name is None else name,
        "ingredients": input_ingredients() if ingredients is None else ingredients,
        "description": input("description: ") if description is None else description,
        "instructions": input("instructions: ") if instructions is None else instructions }
    with session.post(url, files={"image": open("./burger.jpeg", "rb")}, data=recipe) as response:
        try:
            data = response.json()
            return data.get("data"), data.get("error")
        except:
            print(response.text)


def delete_recipe(session, address, rowid):
    url = build_url(address, "recipes/delete")
    with session.post(url + f"/{rowid}", headers={
        "Content-Type": "application/json"
        }) as response:
        try:
            data = response.json()
            return data.get("data"), data.get("error")
        except:
            print(response.text)


def main(argv):
    
    if len(argv) != 2:
        print(f"usage: {os.path.basename(argv[0])} <address>")
        return 0

    address = argv[1]
    username = "admin"# input("username: ")
    password = "admin"# getpass("password: ")

    if session := login(address, username, password):
        while (choice := input("[create/delete/get/all]: ")) not in ["q", "quit"]:
            if choice.lower() == "create":
                recipeid, error = create_recipe(session, address)
                if error:
                    print(error)
                    continue
                print(f"+ created recipe: {recipeid}")
            elif choice.lower().startswith("delete"):
                tokens = choice.split(' ')
                if len(tokens) <= 1:
                    print("missing rowid")
                    continue
                name, error = delete_recipe(session, address, tokens[1])
                if error:
                    print(error)
                    continue
                print(f"- deleted recipe {name}")
            elif choice.lower().startswith("get"):
                tokens = choice.split(' ')
                if len(tokens) <= 1:
                    print("missing rowid")
                    continue
                recipe, error = get_recipe(session, address, tokens[1])
                if error:
                    print(str(error))
                    continue
                print(f"{recipe['name']} - {recipe['id']}")
                print(f" description: {recipe['description']}")
                print(f" instructions: {recipe['instructions']}")
                print(f" image url: {recipe['image']}")
                print(" ingredients:")
                for ingredient in recipe['ingredients']:
                    print(f" - {ingredient['name']}")
            elif choice.lower() == "all":
                recipes, error = all_recipes(session, address)
                if error:
                    print(str(error))
                    continue
                for recipe in recipes:
                    print(f"{recipe['name']} - {recipe['id']}")
                    print(f" description: {recipe['description']}")
                    print(f" instructions: {recipe['instructions']}")
                    print(f" image url: {recipe['image']}")
        logout(address, session)

if __name__ == "__main__":
    try:
        exit(main(sys.argv))
    except KeyboardInterrupt:
        exit(0)
