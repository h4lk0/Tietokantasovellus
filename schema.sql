CREATE TABLE shelters (
    id SERIAL PRIMARY KEY,
    name TEXT,
    info TEXT,
    in_storage BOOLEAN,
    visible BOOLEAN
);

CREATE TABLE tools (
    id SERIAL PRIMARY KEY,
    name TEXT,
    info TEXT,
    amount INTEGER,
    in_storage BOOLEAN,
    visible BOOLEAN
);

CREATE TABLE misc (
    id SERIAL PRIMARY KEY,
    name TEXT,
    info TEXT,
    amount INTEGER,
    in_storage BOOLEAN,
    visible BOOLEAN
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    is_admin BOOLEAN
);

CREATE TABLE loans (
    username TEXT REFERENCES users(username),
    name TEXT,
    amount INTEGER
);
