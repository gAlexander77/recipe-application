drop table if exists users;
drop table if exists recipes;
drop table if exists ingredients;
drop table if exists ratings;

drop view if exists recipe_card;
drop view if exists recipe_full;

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

create table if not exists activity (
	userid integer not null,
	recipeid integer not null,
	rating integer,
	comment text,
	foreign key (userid) references users (rowid) on delete cascade,
	foreign key (recipeid) references recipes (rowid) on delete cascade
);

create view recipe_card as
select recipes.rowid, name, description, recipes.image, userid, username
from recipes left join users on recipes.userid = users.rowid;

create view recipe_full as
select recipes.rowid, name, description, instructions, recipes.image, 
userid, username
from recipes left join users on recipes.userid = users.rowid;

