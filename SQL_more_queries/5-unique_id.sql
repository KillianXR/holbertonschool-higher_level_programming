-- create a "unique_id" table with a id, name the id is unique for all object and is defaut 1
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE,name VARCHAR(256));