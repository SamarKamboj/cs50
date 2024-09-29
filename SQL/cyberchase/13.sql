-- Find the titles of topics including data and aired in/after 2004
SELECT title FROM episodes WHERE topic LIKE "%data%" AND air_date >= '2004-01-01';
