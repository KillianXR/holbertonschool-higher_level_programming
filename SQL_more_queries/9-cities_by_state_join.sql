-- list all cities using subquery to get state name
SELECT cities.id, cities.name AS city_name,
       (SELECT name FROM states WHERE id = cities.state_id) AS state_name
FROM cities
ORDER BY cities.id ASC;
