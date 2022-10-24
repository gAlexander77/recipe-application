import unittest

from tests import create_db
from api.models import *
    
db = create_db()

class Test01Users(unittest.TestCase):

    def test010_create(self):
        userid, error = users.create(db, "user1", "password!")
        self.assertIsNone(error)
        self.assertEqual(userid, 1)

    def test011_create_duplicate_username(self):
        _, error = users.create(db, "user1", "password")
        self.assertIsNotNone(error)
        self.assertEqual(str(error), "UNIQUE constraint failed: users.username")
    
    def test011_create_duplicate_password(self):
        userid, error = users.create(db, "user2", "password")
        self.assertIsNone(error)
        self.assertEqual(userid, 2)
    
    def test020_get_rowid(self):
        user, error = users.get(db, rowid=1)
        self.assertIsNone(error)
        self.assertEqual(user["username"], "user1")
        self.assertEqual(user["password"], md5sum("password!"))

    def test021_get_username(self):
        user, error = users.get(db, username="user1")
        self.assertIsNone(error)
        self.assertEqual(user["username"], "user1")
        self.assertEqual(user["password"], md5sum("password!"))

    def test022_get_nonexist_rowid(self):
        pass
    
    def test023_get_nonexist_username(self):
        pass

    def test030_all(self):
        rows, error = users.all(db)
        self.assertIsNone(error)
        self.assertEqual(len(rows), 2)

    def test040_delete(self):
        username, error = users.delete(db, 1)
        self.assertIsNone(error)
        self.assertEqual(username, "user1")


class Test02Recipes(unittest.TestCase):

    def test010_create(self):
        recipe_id, error = recipes.create(db, 1, "meatballs", "lorem", "ipsum")
        self.assertIsNone(error)
        self.assertEqual(recipe_id, 1) # creating the first recipe

    def test011_create_duplicate_name(self):
        result, error = recipes.create(db, 1, "meatballs", "dope", "dope")
        self.assertIsNotNone(error)
        self.assertEqual(str(error), "UNIQUE constraint failed: recipes.userid, recipes.name")


if __name__ == "__main__":
    unittest.main()
    db.close()
