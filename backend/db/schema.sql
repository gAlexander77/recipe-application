create table if not exists users (
	id text primary key,
	username text unique not null,
	password text
);

create table if not exists recipies (
	id text primary key,
	title text not null,
	instructions text,
	user blob not null,
	foreign key(user) references users(id)
);

create table if not exists ingredients (
	id text primary key,
	name text not null,
	unit text not null,
	quantity integer,
	recipe blob not null,
	foreign key(recipe) references recipies(id)
);
