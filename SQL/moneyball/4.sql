SELECT "first_name", "last_name", "salary" FROM "players"
RIGHT JOIN "salaries" ON "players"."id" = "salaries"."player_id"
WHERE "salaries"."year" = 2001
ORDER BY "salary", "first_name", "last_name", "players"."id"
LIMIT 50;

