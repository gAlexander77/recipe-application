# Source Code
<b>Contributors</b>: <i>Andrew Heckman</i>, <i>Jon Brooks</i>
## Main
Entry point for the code. This is where flask is set up, configurations
are handled, and the initial "api" `Blueprint` object is being mounted.
- `main.py`
## API
This section handles the endpoint logic for flask. 
It uses the functions from `/sql` in order to commit
transactions on the sqlite3 database
- `__init__.py`
- `ingredients.py`
- `recipes.py`
- `users.py`
- `util.py`
## Database (SQL)
This section defines logic to easily and ergonomically
make transactions on a sqlite3 database. Default locations
for the database file are written into `__init__.py`
- `__init__.py`
- `insert.py`
- `select.py`
- `delete.py`
- `util.py`
