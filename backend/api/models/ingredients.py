def create(db, recipeid, name):
    from api.models import insert
    return insert(db, recipeid, {"name": name})
