# Recipe Project | Backend API
<b>Contributors</b>: Andrew Heckman, Jon Parker Brooks

## Dependencies
- Python3.10
- SQLite3 (included with python)
- Flask 2.2

## Testing
In order to get going quickly in the frontend with some sample data, run `python3 ./test/gendb.py` before running the server

## How To Use
In order to run the server you must have flask installed: 
`python3 -m pip install --user flask==2.2.2`. \ 
If flask is installed, you may run the program in the "backend/" directory like so:
`python3 -m flask --app ./src/main.py run`

## Active API Routes
```
GET:
	- /api/recipes
	  GET parameter filters
	  -- id: recipe id
	  -- user: id of user who posted recipe
	  -- title: title of recipe
	  -- steps: content of the instructions of the recipe
	  -- rating: numerical rating of recipe (0-10 for stars & half-stars)
	  
	  example:
		
		> http://localhost:5000/api/recipes?title=Pot%20Roast
		this url will filter the data returned by recipes with
		"Pot Roast" in the title, %20 is the url character for space
		
		> http://localhost:5000/api/recipes?rating=4
		this url will filter the data returned by recipes rated 4
		or 2 out of 5 stars
POST:
	user:
	- /api/create/user

	recipe:
	- /api/create/recipe
	  JSON POST parameter requirements
	  -- user: id of user creating recipe
	  -- title: title of recipe
	  -- steps: text content of instructions
	  -- ingredients: JSON object where the keys are ingredient
	                  names, and the values are units + count

	  note: try to make ingredient names singular instead of plural.
	        the frontend can handle adding the 's' based on count value
	  
	  example:
	    > json payload:
		{
			"user": "c5d1804bd5fb4e739fa524eb5b04cdc1", // the user id should be available if the user is logged in
			"title": "Pot Roast v2",
			"steps": "1. lawyer up\n2. hit the gym\n3. delete facebook",
			"ingredients": {
				"roast beef": ["lbs", 2],
				"carrot": ["-", 5], // for no unit, a dash is accepted
				"broth": ["floz", 6]
			}
		}
	
	- /api/delete/recipe/<id>:
	  POST parameter requirements
	  -- none
	  
	  note: all you have to do is supply the recipe id in the url
	        after the word recipe (where it says <id>), and make
			sure that react is sending a POST request in case a
			user somehow gets to the page using a browser
```
