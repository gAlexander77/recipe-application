drop table if exists users;
drop table if exists recipes;
drop table if exists ingredients;
drop table if exists ratings;

create table users (
	rowid integer primary key autoincrement,
	username text unique not null,
	password text not null,
	created integer not null default (strftime('%s'))
);

create table recipes (
	rowid integer primary key autoincrement,
	userid integer not null,
	name text not null,
	description text not null,
	instructions text not null,
	created integer not null default (strftime('%s')),
	unique(userid, name),
	foreign key (userid) references users (rowid) on delete cascade
);

create table ingredients (
	rowid integer primary key autoincrement,
	recipeid integer not null,
	name text not null,
	foreign key (recipeid) references recipes (rowid) on delete cascade
);

create table ratings (
	userid integer not null,
	recipeid integer not null,
	rating integer not null,
	foreign key (userid) references users (rowid) on delete cascade,
	foreign key (recipeid) references recipes (rowid) on delete cascade
);

insert into users (username, password) values ("admin", "21232f297a57a5a743894a0e4a801fc3");
