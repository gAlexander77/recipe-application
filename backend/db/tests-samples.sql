INSERT INTO users (username, password, created)
VALUES (
	"admin", 
	"fb001dfcffd1c899f3297871406242f097aecf1a5342ccf3ebcd116146188e4b",
	0
);

INSERT INTO recipes (userid, name, ingredients, description, instructions, image)
VALUES (1, "hello world", "no\nway", "goodbye world", "nope", "i.jpg");
INSERT INTO recipes (userid, name, ingredients, description, instructions, image)
VALUES (1, "goodbye world", "yes\nway", "mmm", "nnn", "o.jpg");

INSERT INTO ratings (userid, recipeid, rating)
VALUES (1, 1, 5);
