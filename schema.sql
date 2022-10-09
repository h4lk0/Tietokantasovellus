CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    is_admin BOOLEAN
);

CREATE TABLE loans (
    user_id REFERENCES users(id)
    object_id REFERENCES inventory(item_id)
);

CREATE TABLE item_names (
    name_id SERIAL PRIMARY KEY,
    item_name TEXT UNIQUE,
);

CREATE TABLE item_categories (
    category_id SERIAL PRIMARY KEY,
    category_name TEXT UNIQUE,
);

CREATE TABLE inventory (
    item_id SERIAL PRIMARY KEY,
    item_type REFERENCES item_names(name_id),
    category REFERENCES item_categories(category_id),
    information TEXT,
    in_storage BOOLEAN DEFAULT TRUE
);
