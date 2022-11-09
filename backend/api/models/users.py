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
def create(db, username, password):

    from api.models import insert
    from hashlib import md5

    return insert(db, "users", {
        "username": username, 
        "password": md5(password.encode("utf-8")).digest().hex()
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
    from api.models import delete
    return delete(db, "users", rowid, "username")
