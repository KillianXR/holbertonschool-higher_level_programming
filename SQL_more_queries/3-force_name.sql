-- script that create a force_name table with id, name info who can't be NULL
CREATE TABLE IF NOT EXIST force_name (id INT,name VARCHAR(256) NOT NULL);