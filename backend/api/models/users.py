from api.models import success, failure, md5sum
from api import db


def create(db, username, password, image=None):
    try:
        row = db.execute(
            """insert into users (username, password) values (?, ?)
            returning rowid""",
            (username, md5sum(password))).fetchone()
    except Exception as error:
        return failure(error)
    db.commit()
    return success(row["rowid"])


def delete(db, rowid):
    try:
        row = db.execute(
            """delete from users where rowid = ?
            returning username""", 
            (rowid,)).fetchone()
    except Exception as error:
        return failure(error)
    db.commit()
    return success(row["username"])


def get(db, rowid=None, username=None):
   
    field, query = ("rowid", rowid) if rowid is not None else ("username", username)
    if query is None:
        return failure("username or rowid is required")

    try:
        row = db.execute(f"select * from users where {field} = ?", 
            (query,))
    except Exception as error:
        return failure(error)

    user = row.fetchone()
    return success({
        "id": user["rowid"],
        "username": user["username"],
        "password": user["password"],
        "created": user["created"] }) if user else failure("user does not exist")


def all(db):
    
    try:
        rows = db.execute("select * from users")
    except Exception as error:
        return failure(error)

    return success(list({
        "id": user["rowid"], 
        "username": user["username"], 
        "created": user["created"]
        } for user in rows.fetchall()))
