from .util import valid_table, db_pass, db_fail

DEBUG = 0

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
ORDER BY %s DESC"""
RECIPE_INGREDIENTS_SQL = """SELECT
ingredients.id AS id, name
FROM recipes_ingredients
INNER JOIN ingredients ON ingredients.id = recipes_ingredients.ingredient"""
INGREDIENT_RECIPES_SQL = """SELECT
recipes.id, title, description, AVG(rating) as rating
FROM recipes
INNER JOIN recipes_ingredients ON recipes.id = recipes_ingredients.recipe
INNER JOIN users_recipes ON recipes.id = users_recipes.recipe
GROUP BY recipes.id"""

def query(sql, fields, expression):
    items = list(filter(lambda t: t[1] is not None, fields.items()))
    if len(items) > 0:
        filtered = " WHERE " + " AND ".join(expression % (k, v) for k, v in items)
        if "GROUP" in sql:
            halves = sql.split('GROUP')
            sql = halves[0].strip() + filtered + " GROUP" + halves[1]
        else:
            sql += filtered
    return sql


def select(db, sql, fields, single=False):

    expression =  "%s LIKE '%%%s%%'"
    sql = query(sql, fields, expression)

    if DEBUG: print(sql)

    try:
        rows = db.execute(sql)
    except Exception as error:
        return db_fail(error)

    return db_pass(rows.fetchone() if single else rows.fetchall())


def user(db, id=None, username=None):
    if id is not None or username is not None:
        return select(db, USERS_SQL, {
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
        name = name if name is None else name.capitalize().strip()
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


def recipes(db, id=None, title=None, description=None, userid=None, username=None, rating=None, sort_by=None):
    sort_by = "created" if sort_by is None else sort_by
    sort_by = "recipes." + sort_by if sort_by != "rating" else sort_by
    return select(db, RECIPES_SQL % sort_by, {
        "recipes.id": id, 
        "title": title, 
        "description": description, 
        "recipes.user": userid,
        "username": username,
        "rating": rating
    })



def ingredients(db, id=None, name=None):
    name = name if name is None else name.capitalize().strip()
    return select(db, INGREDIENTS_SQL, {
        "id": id,
        "name": name
    })


def recipe_ingredients(db, recipe):
    return select(db, RECIPE_INGREDIENTS_SQL, {
        "recipes_ingredients.recipe": recipe
    })


def ingredient_recipes(db, ingredient):
    return select(db, INGREDIENT_RECIPES_SQL, { 
        "recipes_ingredients.ingredient": ingredient 
    })
