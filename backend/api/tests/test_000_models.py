from api import models


def test_000_sql_filter():
    assert models.__sql_filter({"username": "admin"}) == " WHERE username = 'admin'"

def test_001_sql_filter_multi():
    assert models.__sql_filter({"key1": "val1", "key2": "val2"}) == " WHERE key1 = 'val1' AND key2 = 'val2'"
