create table if not exists users (
	id integer primary key autoincrement,
	username text unique,
	password text,
	created integer
);

create table if not exists recipes (
	id integer primary key autoincrement,
	userid integer,
	name text,
	ingredients text,
	description text,
	instructions text,
	image text,
	created integer,
	foreign key (userid) references users (id)
);

create table if not exists ratings (
	id integer primary key autoincrement,
	userid integer,
	recipeid integer,
	rating real,
	unique(userid, recipeid),
	foreign key (userid) references users (id),
	foreign key (recipeid) references recipes (id)
);

create table if not exists comments (
	id integer primary key autoincrement,
	userid integer,
	recipeid integer,
	comment text,
	created integer,
	foreign key (userid) references users (id),
	foreign key (recipeid) references recipes (id)
);

create view if not exists full_recipes as
select recipes.id as id, users.id as userid,
name, username, recipes.created as created, 
ingredients, description, instructions, image
from recipes
left join users on recipes.userid = users.id;

create view if not exists full_comments as
select * from comments
left join recipes on comments.recipeid = recipes.id
left join users on comments.userid = users.id;

create view avg_ratings as
select recipeid, avg(rating) as rating 
from ratings
group by recipeid;
