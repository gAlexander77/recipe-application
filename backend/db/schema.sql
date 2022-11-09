drop table if exists users;
drop table if exists recipes;
drop table if exists ratings;
drop table if exists comments;
drop table if exists ingredients;

drop view if exists interactions;

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

create view interactions
select * from users
left join ratings on users.rowid = ratings.userid
left join comments on users.rowid = comments.userid;
