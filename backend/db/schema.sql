drop table if exists users;
drop table if exists recipes;
drop table if exists ingredients;
drop table if exists interaction;

drop view if exists recipe_cards;
drop view if exists recipe_pages;

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

create table if not exists ingredients (
	rowid integer primary key autoincrement,
	recipeid integer not null,
	name text not null,
	foreign key (recipeid) references recipes (rowid) on delete cascade
);

create table if not exists interaction (
	userid integer not null,
	recipeid integer not null,
	rating integer,
	comment text,
	created integer not null default (strftime('%s')),
	foreign key(userid) references users(rowid) on delete cascade,
	foreign key(recipeid) references recipes(rowid) on delete cascade
);

create view recipe_cards as
select recipes.rowid, name, description, recipes.image, userid, username
from recipes 
left join users on recipes.userid = users.rowid
left join interaction on recipes.rowid = interaction.recipeid;

create view recipe_pages as
select recipes.rowid, name, description, instructions, recipes.image, 
userid, username
from recipes 
left join users on recipes.userid = users.rowid
left join interaction on recipes.rowid = interaction.recipeid;
