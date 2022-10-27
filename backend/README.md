# API Documentation
Contributors: Jon Brooks
# Tests
- [ ] Models
  - [x] Users
  - [ ] Recipes
  - [ ] Ingredients
  - [ ] Ratings
- [ ] Routes (?)
# Features
- [x] Create user
- [x] Create recipe
  - [x] upload Image
  - [ ] delete Image
- [x] Delete recipe
- [ ] Rate recipe
# Structure
Here's is the <i>TL;DR:</i> The main source code is located in the `api/`
directory. In there you will find two subdirectories: `models/` and `routes/`.
There's also two other files of interest called `__init__.py`, and `db.py`.
The `models` directory is for the database interface. In this file we do
in a sense "model" the tables of the database into code, which we use as a
pipe and filter into the next module `routes`, which is responsible 
for handling requests from the frontend. See below for more details.
`__init__.py` is like the `main.py` or the main function of the program, to
try and follow the execution stack, maybe start there. There is a factory 
function<sup>[1]</sup> in there called `create_app()` which I use to initialize
Flask. `db.py` is just a collection of helper functions for the database.  
<sup><sub>- [1] A factory function is something the library will call at runtime to run some
configuration that takes more than some values to set up. In this case, we need to
do a number of things before returning the app object so it provides us with the `create_app()`
interface function to do those things. pretty nice!</sub></sup>
# Routes
...Coming soon
# Models
...Coming soon
