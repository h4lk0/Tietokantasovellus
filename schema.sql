CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    is_admin BOOLEAN DEFAULT FALSE
);

CREATE TABLE item_names (
    name_id SERIAL PRIMARY KEY,
    item_name TEXT UNIQUE
);

CREATE TABLE item_categories (
    category_id SERIAL PRIMARY KEY,
    category_name TEXT UNIQUE
);

CREATE TABLE inventory (
    item_id SERIAL PRIMARY KEY,
    item_type INTEGER REFERENCES item_names(name_id),
    category INTEGER REFERENCES item_categories(category_id),
    information TEXT,
    in_storage BOOLEAN DEFAULT TRUE
);

CREATE TABLE loans (
    loan_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    object_id INTEGER REFERENCES inventory(item_id)
);
