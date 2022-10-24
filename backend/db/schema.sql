create table if not exists users (
	rowid integer primary key autoincrement,
	username text unique not null,
	password text not null,
	created integer not null default (strftime('%s'))
);

create table if not exists recipes (
	rowid integer primary key autoincrement,
	userid integer not null,
	name text not null,
	description text not null,
	instructions text not null,
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

create table if not exists ratings (
	userid integer not null,
	recipeid integer not null,
	rating integer not null,
	foreign key (userid) references users (rowid) on delete cascade,
	foreign key (recipeid) references recipes (rowid) on delete cascade
);
