-- script that create a database "hbtn_0d_usa" with a table "states"
-- who contain a id who can't be null, a number will be automatically assigned
-- and got a primary to compare with other object and don't get 2 times the same id
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,name VARCHAR(256));