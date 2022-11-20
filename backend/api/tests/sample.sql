INSERT INTO users (username, password) 
VALUES ("user1", "286755fad04869ca523320acce0dc6a4");
INSERT INTO users (username, password) 
VALUES ("user2", "286755fad04869ca523320acce0dc6a4");

INSERT INTO recipes (userid, name, description, instructions) 
VALUES (1, "Sandwich", "test sandwich", "make the sandwich");
INSERT INTO recipes (userid, name, description, instructions) 
VALUES (2, "other recipe", "I am a test", "do not make");

INSERT INTO ingredients (recipeid, name)
VALUES (1, "bread");
INSERT INTO ingredients (recipeid, name)
VALUES (1, "cheese");
INSERT INTO ingredients (recipeid, name)
VALUES (1, "turkey");

INSERT INTO comments (userid, recipeid, comment)
VALUES (2, 1, "nice sandwich");

INSERT INTO ratings (userid, recipeid, rating)
VALUES (1, 2, 3);
INSERT INTO ratings (userid, recipeid, rating)
VALUES (2, 1, 4);
