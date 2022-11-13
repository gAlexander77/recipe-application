drop table if exists users;
drop table if exists recipes;
drop table if exists ratings;
drop table if exists comments;
drop table if exists ingredients;

drop view if exists recipe_cards;

drop view if exists recipe_comments;
drop view if exists recipe_ratings;
drop view if exists user_comments;
drop view if exists user_ratings;

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
	rating real not null,
	foreign key (userid) references users (rowid) on delete cascade,
	foreign key (recipeid) references recipes (rowid) on delete cascade
);

create table comments (
	rowid integer primary key autoincrement,
	userid integer not null,
	recipeid integer not null,
	comment text,
	created integer not null default (strftime('%s')),
	foreign key (userid) references users (rowid) on delete cascade,
	foreign key (recipeid) references recipes (rowid) on delete cascade
);

create table ingredients (
	rowid integer primary key autoincrement,
	recipeid integer not null,
	name text not null,
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

create view recipe_comments as
select comment, username, recipeid, 
comments.created as created
from comments
left join users on users.rowid = comments.userid;

create view user_comments as
select comment, username, userid, 
comments.created as created
from comments
left join users on users.rowid = comments.userid;

create view recipe_ratings as
select rating, username, recipeid
from ratings
left join users on users.rowid = ratings.userid;

create view user_ratings as
select rating, username, userid
from ratings
left join users on users.rowid = ratings.userid;
