# Recipedia Configuration
Contributor: Jon Parker Brooks

## API
The file to configure the API for the backend application
is called `config.json`. it contains all the valid key-value
pairs applicable to recipedia.
- DB_PATH: path to the server database
- SCHEMA_PATH: path to the file describing the server schema
- UPLOADS_DIR: path to the folder where recipe images are uploaded
- SERVE_UPLOADS: if true Flask will serve the images, otherwise, another service must host them

## uWSGI
The configuration file for uwsgi also lives in this directory. it
is called `wsgi.json`. read up on uwsgi for more information about
the parameters in this file, or run `uwsgi --help`
