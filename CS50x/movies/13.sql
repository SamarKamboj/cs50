SELECT DISTINCT people.name FROM stars
JOIN people ON people.id = stars.person_id
WHERE movie_id IN
(SELECT movie_id FROM stars JOIN people ON stars.person_id = people.id
WHERE name = (SELECT name FROM people WHERE name = "Kevin Bacon" AND birth = 1958)) AND name != "Kevin Bacon";