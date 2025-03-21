-- show all tv_genre and the numbers of show of the designed genre 
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
HAVING COUNT(tv_genres.id) > 0
ORDER BY number_of_shows DESC;
