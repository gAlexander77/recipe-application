from api import models

# create:
# makes a new user
#  inputs:
#   - current database object
#   - new user's username
#   - new user's password
#  side effects:
#   - creates a table in the database
#  output:
#   - value of new user's id
def insert(db, username, password):
    return models.insert(db, "users", {
        "username": username,
        "password": models.md5sum(password)
    })


# delete:
# deletes the specified user
#  inputs:
#    - user's id
#  side effects:
#    - removes a table from the database
#  output:
#    - username of user deleted
def delete(db, rowid):
    return models.delete(db, "users", rowid, "username")


# select
# gets a user row based off rowid or username
def select(db, rowid=None, username=None):
    assert rowid is not None or username is not None
    return models.select(db, "users", {
        "rowid": rowid,
        "username": username
    })
