from .util import valid_table, db_pass, db_fail


# users and ingredients are ez
USERS_SQL = "SELECT id, username FROM users"
INGREDIENTS_SQL = "SELECT id, name FROM ingredients"

# recipes are a bit complex
RECIPE_SQL = """SELECT
recipes.id, title, description, recipes.updated, 
recipes.user AS userid, username,
AVG(rating) AS rating
FROM recipes
LEFT JOIN users ON recipes.user = users.id
INNER JOIN users_recipes ON recipes.id = users_recipes.recipe"""
RECIPES_SQL = """SELECT
recipes.id, title, description, recipes.updated, 
recipes.user AS userid, username,
AVG(rating) AS rating
FROM recipes
LEFT JOIN users ON recipes.user = users.id
INNER JOIN users_recipes ON recipes.id = users_recipes.recipe
GROUP BY recipes.id
ORDER BY rating DESC"""
RECIPE_INGREDIENTS_SQL = """SELECT
ingredients.id as id, name
FROM recipes_ingredients
INNER JOIN ingredients ON ingredients.id = recipes_ingredients.ingredient"""


def query(sql, fields, expression):
    items = list(filter(lambda t: t[1] is not None, fields.items()))
    if len(items) > 0:
        return sql + " WHERE " + " AND ".join(expression % (k, v) for k, v in items)
    return sql


def select(db, sql, fields, single=False):

    expression =  "%s = '%s'" if single else "%s LIKE '%%%s%%'"
    sql = query(sql, fields, expression)

    try:
        rows = db.execute(sql)
    except Exception as error:
        return db_fail(error)

    return db_pass(rows.fetchone() if single else rows.fetchall())


def user(db, id=None, username=None):
    if id is not None or username is not None:
        return select(db, USER_SQL, {
            "id": id, 
            "username": username, 
        }, single=True)
    return db_fail("id or username required")


def recipe(db, id=None, title=None, user=None):
    if id is not None or name is not None or user is not None:
        return select(db, RECIPE_SQL, {
            "recipes.id": id, 
            "title": title, 
            "user": user 
        }, single=True)
    return db_fail("id or title or user required")


def ingredient(db, id=None, name=None):
    if id is not None or name is not None:
        return select(db, INGREDIENTS_SQL, {
            "id": id,
            "name": name
        }, single=True)
    return db_fail("id or name required")


def users(db, id=None, username=None):
    return select(db, USERS_SQL, {
        "id": id, 
        "username": username
    })


def recipes(db, id=None, title=None, description=None, user=None, rating=None):
    return select(db, RECIPES_SQL, {
        "id": id, 
        "title": title, 
        "description": description, 
        "user": user, 
        "rating": rating
    })


def ingredients(db, id=None, name=None):
    return select(db, INGREDIENTS_SQL, {
        "id": id,
        "name": name
    })

def recipe_ingredients(db, recipe):
    return select(db, RECIPE_INGREDIENTS_SQL, {
        "recipes_ingredients.recipe": recipe
    })
