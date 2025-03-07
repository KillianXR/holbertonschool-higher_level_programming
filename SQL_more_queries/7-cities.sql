-- script that create a database "hbtn_0d_usa" with a table "cities"
-- with a row, id automatically attributed and unique for all object can't be NULL
-- a row, for the state_id who can't be NULL to reference a city with a state with a foreign key
-- and a row with the name of the city can't be NULL too 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);