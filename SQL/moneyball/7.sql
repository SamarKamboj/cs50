SELECT "p"."first_name", "p"."last_name" FROM "salaries" AS "s"
LEFT JOIN "players" AS "p" ON "p"."id" = "s"."player_id"
WHERE "s"."salary" IN (
    SELECT MAX("salary") FROM "salaries"
);
