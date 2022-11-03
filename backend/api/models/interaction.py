from api.models import success, failure
from api import db

def create(db, userid, recipeid, comment=None, rating=None):
    try:
        rowid = db.execute("""insert into interaction
                   (userid, recipeid, rating, comment) 
                   values (?, ?, ?, ?)
                   returning rowid""",
                   (userid, recipeid, rating, comment))
        db.commit()
    except Exception as error:
        return failure(str(error))
    return success(rowid)


def update(db, rowid, comment=None, rating=None):
    pass
