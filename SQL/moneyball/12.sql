WITH "least_expensive_per_hit" AS (
    SELECT "players"."id", "players"."first_name", "players"."last_name"
    FROM "players"
    JOIN "performances" ON "performances"."player_id" = "players"."id"
    JOIN "salaries" ON "salaries"."player_id" = "players"."id" AND "salaries"."year" = "performances"."year"
    WHERE "salaries"."year" = 2001 AND "performances"."year" = 2001 AND "performances"."H" > 0
    ORDER BY ("salaries"."salary" / "performances"."H"), "players"."id"
    LIMIT 10
),
"least_expensive_per_rbi" AS (
    SELECT "players"."id", "players"."first_name", "players"."last_name"
    FROM "players"
    JOIN "performances" ON "performances"."player_id" = "players"."id"
    JOIN "salaries" ON "salaries"."player_id" = "players"."id" AND "salaries"."year" = "performances"."year"
    WHERE "salaries"."year" = 2001 AND "performances"."year" = 2001 AND "performances"."RBI" > 0
    ORDER BY ("salaries"."salary" / "performances"."RBI"), "players"."id"
    LIMIT 10
)
SELECT "least_expensive_per_hit"."first_name", "least_expensive_per_hit"."last_name"
FROM "least_expensive_per_hit"
INTERSECT
SELECT "least_expensive_per_rbi"."first_name", "least_expensive_per_rbi"."last_name"
FROM "least_expensive_per_rbi"
ORDER BY "least_expensive_per_hit"."last_name", "least_expensive_per_hit"."first_name";
