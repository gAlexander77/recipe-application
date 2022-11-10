drop table if exists users;
drop table if exists recipes;
drop table if exists ratings;
drop table if exists comments;
drop table if exists ingredients;

drop view if exists recipe_cards;
drop view if exists recipe_comment_count;

create table users (
	rowid integer primary key autoincrement,
	username text unique not null,
	password text not null,
	image text,
	created integer not null default (strftime('%s'))
);

create table recipes (
	rowid integer primary key autoincrement,
	userid integer not null,
	name text not null,
	description text not null,
	instructions text not null,
	image text,
	created integer not null default (strftime('%s')),
	unique(userid, name),
	foreign key (userid) references users (rowid) on delete cascade
);

create table ratings (
	rowid integer primary key autoincrement,
	userid integer not null,
	recipeid integer not null,
	score real not null,
	unique(userid, recipeid),
	foreign key (userid) references users (rowid) on delete cascade,
	foreign key (recipeid) references recipes (rowid) on delete cascade
);

create table comments (
	rowid integer primary key autoincrement,
	userid integer not null,
	recipeid integer not null,
	content text,
	created integer not null default (strftime('%s')),
	unique(userid, recipeid),
	foreign key (userid) references users (rowid) on delete cascade,
	foreign key (recipeid) references recipes (rowid) on delete cascade
);

create table ingredients (
	rowid integer primary key autoincrement,
	recipeid integer not null,
	name text not null,
	unique(recipeid, name),
	foreign key (recipeid) references recipes (rowid) on delete cascade
);


create view recipe_cards as
select name, username, description, instructions,
recipes.userid as userid,
recipes.rowid as rowid,
recipes.image as image,
recipes.created as created
from recipes 
join users on recipes.userid = users.rowid;

create view recipe_comment_count as
select count(comments.rowid)
from recipes
join comments on recipes.rowid = comments.recipeid;
