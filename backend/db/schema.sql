create table if not exists users (
	id integer primary key,
	username text not null,
	password text
);

create table if not exists recipies (
	id integer primary key,
	title text not null,
	instructions text,
	user integer not null,
	foreign key(user) references users(id)
);

create table if not exists ingredients (
	id integer primary key,
	name text not null,
	unit text not null,
	quantity integer,
	recipe integer not null,
	foreign key(recipe) references recipies(id)
);
