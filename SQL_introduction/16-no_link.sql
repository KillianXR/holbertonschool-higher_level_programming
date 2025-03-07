-- a script that lists all records of the table second_table of the database 
SELECT score, name FROM second_table where name IS NOT NULL and name != '' ORDER BY score DESC