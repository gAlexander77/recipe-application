create table if not exists users (
	id text primary key,
	username text unique not null,
	password text
);

create table if not exists recipes (
	id text primary key,
	user text not null,
	title text unique not null,
	steps text not null,
	rating integer not null,
	foreign key(user) references users(id)
);

create table if not exists ingredients (
	id text primary key,
	name text unique not null,
	rating integer not null
);

create table if not exists recipes_ingredients (
	id text primary key,
	recipe text not null,
	ingredient text not null,
	units text,
	count real not null,
	foreign key(recipe) references recipes(id),
	foreign key(ingredient) references ingredients(id)
);

create table if not exists users_recipes (
	id text primary key,
	user text not null,
	recipe text not null,
	rating integer not null,
	marked integer not null,
	foreign key(user) references users(id),
	foreign key(recipe) references recipies(recipe)
);
