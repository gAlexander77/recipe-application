create table if not exists users (
	id text primary key,
	username text unique not null,
	password text not null,
	created integer not null,
	updated integer not null
);

create table if not exists recipes (
	id text primary key,
	name text not null,
	description text not null,
	instructions text not null,
	created integer not null,
	updated integer not null,
	user text not null,
	constraint fk_user 
		foreign key(user) 
		references users(id)
		on delete cascade
);

create table if not exists ingredients (
	id text primary key,
	name text unique not null
);

create table if not exists recipes_ingredients (
	id text primary key,
	recipe text not null,
	ingredient text not null,
	constraint fk_recipe 
		foreign key(recipe) 
		references recipes(id)
		on delete cascade,
	constraint fk_ingredient
		foreign key(ingredient)
		references ingredients(id)
		on delete cascade
);

create table if not exists users_recipes (
	id text primary key,
	user text not null,
	recipe text not null,
	rating integer not null,
	pinned integer not null,
	constraint fk_user
		foreign key(user) 
		references users(id)
		on delete cascade,
	constraint fk_recipe 
		foreign key(recipe) 
		references recipes(id)
		on delete cascade
);
