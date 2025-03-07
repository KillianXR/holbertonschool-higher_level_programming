-- create seconds_table if not exist with id, name, score in it
CREATE table IF NOT EXISTS seconds_table (id INT, name VARCHAR(256), score INT);
--
INSERT INTO seconds_table (id, name, score) VALUES (1, 'John', 10);
INSERT INTO seconds_table (id, name, score) VALUES (2, 'Alex', 3);
INSERT INTO seconds_table (id, name, score) VALUES (3, 'Bob', 14);
INSERT INTO seconds_table (id, name, score) VALUES (4, 'George', 8);
