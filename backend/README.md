# Recipedia: Backend
Contributor: Jon Parker Brooks

## Set Up:
__Recipedia__ uses the _Flask 2.2.X_ library which is written in _Python_.
To get started, you must have a valid _Python_ interpreter >= 3.6.

First, we need to set up the virtual environment for the packages
we are using. Do so in the current directory like this: 
`python3 -m venv venv`. there should now be a directory called
`venv/`.

Next, we activate the virtual environment, this basically points our 
system at the `venv/` directory for any resource that has to do with python.
Activate the virtual environment like this: `source venv/bin/activate`

Last, we should now have a command prompt that starts with: `(venv)`.
At this point, you can install the dependencies, go ahead and run:
`python -m pip install -r requirements.txt` to install all the
needed libraries for the application into the virtual environment.

You will need the virtual environment to be activated for _Testing_
and using the _Development Application_, but not the 
_Production Application_. To deactivate the environment, run:
`deactivate`

### Testing
To run unit tests, in the current directory, run: `pytest -vv`

### Start Development Application
To start the dev server for testing, in the current directory, run: 
`python -m flask --app api run`. you can optionally supply `--host` or
`--port` parameters after `run`. this will start the application
on localhost port 5000 by default.

### Start Production Application
To start the production environment, you must install _uwsgi_ and
_nginx_. in `/etc/nginx/nginx.conf`, configure 
`uwsgi_passthru unix:///tmp/recipedia.sock` to point nginx at this
application. run: `uwsgi --json etc/wsgi.json` in the current
directory to start the server, then start nginx.

# API Reference
_note: pay attention to POST types, incorrect encoding will cause 500 errors_
- x-www-form-urlencoded: default POST type - `<form method="POST" action="/api/...">`
- multipart/form-data: POST type for files and images - `<form method="POST" action="/api/..." enctype="multipart/form-data">`
- application/json: JSON encoded POST body - `axios.post(...) or fetch(...)`

- __Accounts__: User stats and data, Login, Logout
  - __Index__:
    - url: `/api/accounts/`
	- type: GET
	- parameters: none
	- returns: all current user info and recipes
	- description: this is the API endpoint for the user's account page
  - __Login__:
    - url: `/api/accounts/login`
    - type: POST (application/json)
	- parameters: `username: <username string>, password: <password string>`
	- returns: user's ID
	- description: authenticate a user and start a session for them.
  - __Logout__:
    - url: `/api/accounts/logout/<id>`
    - type: POST (x-www-form-urlencoded)
	- parameters: none
	- returns: user's username
	- description: ends a users session, supply the user ID in the URL

- __Comments__: Get all by userID, Get all by recipeID, Create, Delete
  - __Index__:
    - url: `/api/comments/`
	- type: GET
	- parameters: none
	- returns: all comments from the current logged in user
  - __Recipe__:
    - url: `/api/comments/<id>`
	- type: GET
	- parameters: none
	- returns: all comments from the recipe ID supplied in the URL
	- description: get all comments for the recipe on the recipe page
  - __Create__:
    - url: `/api/comments/create`
	- type: POST (application/json)
	- parameters: `recipeid: <id>, comment: <comment string>`
	- returns: id of newly created comment
	- description: create a new comment on a recipe post
  - __Delete__:
    - url: `/api/comments/delete/<id>`
	- type: POST (x-www-form-urlencoded)
	- parameters: none
	- returns: text of deleted comment
	- description: delete a comment from the database

- __Ratings__: Create, Delete
  - __Create__:
    - url: `/api/ratings/create`
	- type: POST (application/json)
	- parameters: `recipeid: <id>, rating: <rating (0-5)>`
	- returns: id of new rating
	- description: rate a recipe
  - __Delete__:
    - url: `/api/ratings/delete/<id>`
	- type: POST (x-www-form-urlencoded)
	- parameters: none
	- returns: value of deleted rating
	- description: unrate a recipe

- __Recipes__: Get all, Get by ID, Create, Delete
  - __Index__:
    - url: `/api/recipes/`
	- type: GET
	- parameters: none
	- returns: all recipes from the database and their average ratings
	- description: this is for the index page on the frontend
  - __Recipe__:
    - url: `/api/recipes/<id>`
	- type: GET
	- parameters: none
	- returns: the specified recipe from the ID in the URL
	- description: this is for the recipe page on the frontend
  - __Create__:
    - url: `/api/recipes/create`
	- type: POST (multipart/form-data)
	- parameters: `name: <recipe title>, ingredients: <array of ingredient strings>, description: <text description of recipe>, instructions: <text instructions>, image: <image for recipe>`
	- returns: id of newly created recipe
	- description: endpoint for recipe creation, make sure to use a multipart/form-data POST to upload the image
  - __Delete__:
    - url: `/api/recipes/delete/<id>`
	- type: POST (x-www-form-urlencoded)
	- parameters: none
	- returns: title of deleted recipe
    - description: endpoint to remove a recipe from the database

- __Users__: Create, Delete
  - __Create__:
    - url: `/api/users/create`
	- type: POST (application/json)
	- parameters: `username: <username string>, password: <password string>`
	- returns: id of newly created user
	- description: endpoint to create a new user
  - __Delete__:
    - url: `/api/users/delete/<id>`
	- type: POST (x-www-form-urlencoded)
	- parameters: none
	- returns: username of deleted user
	- description: endpoint to delete a user
