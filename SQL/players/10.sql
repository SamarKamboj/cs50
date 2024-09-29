-- Fetch name of the player/s who born between 2000 and 2003 (inclusive) having the maximum weight
SELECT "first_name", "last_name", MAX("weight") AS "Maximum Weight" FROM "players" WHERE "birth_year" BETWEEN 2000 AND 2003;
