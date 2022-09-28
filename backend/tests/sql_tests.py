#!/usr/bin/env python3

import os
import sys

# add source code directory to system path for this program
if os.path.isdir("../src"): sys.path.append("../src")
elif os.path.isdir("./src"): sys.path.append("./src")

import sql


TEST_PASSED = "[\033[32mPASSED\033[0m]"
TEST_FAILED = "[\033[31mFAILED\033[0m]"

# write tests here
# example
def test_insert_user(db, username, password, expected, context=None):
    query = sql.insert_user(db, username, password)
    success = query["ok"] == expected
    if context is not None:
        if query["ok"]:
            return success and context == query["data"]
        else:
            return success and context == query["error"]
    return success


# add tests here
TESTS = {
    test_insert_user: [
        # insert user in new db should work
        ("username", "password", True),
        # should not be able to insert multiple users
        ("username", "password", False, "UNIQUE constraint failed: users.username"),
        # should be able to insert user with identical password
        ("username1", "password", True),
        # should not be able to insert empty username
        ("", "password", False, "username must be > 3 characters"),
        # should be able to insert null password
        ("username2", "", True)
    ]
    # TODO for the rest of the DB functions
    # like test_select_user or test_insert_recipe, etc
}
TESTDB = "./tests/testdb.sqlite3"


if __name__ == "__main__":

    db = sql.load_database(TESTDB, sql.SCHEMA)

    # run all tests for sql.py
    # to add a test, all you need to do is add it 
    # to the TESTS dict
    for test, inputs in TESTS.items():
        print("[%s]:" % test.__name__) # .__name__ gives us the function name
        for i, result in enumerate(map(lambda input: test(db, *input), inputs)):
            print("  TEST", i + 1, '->', TEST_PASSED if result else TEST_FAILED)

    # remove test db
    os.remove(TESTDB)
    db.close()
