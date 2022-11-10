from api import models

def insert(db, recipeid, name):
    return models.insert(db, recipeid, {
        "recipeid": recipeid,
        "name": name
    })

def query(db, recipeid=None):
    assert recipeid is not None
    return models.query(db, "ingredients", {"recipeid": recipeid})
