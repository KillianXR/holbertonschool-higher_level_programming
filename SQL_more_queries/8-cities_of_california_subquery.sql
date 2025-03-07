-- script that list all the cities of california order by cities id 
-- select who city go with who states with a subquery
SELECT id, name FROM cities 
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;