SELECT "city", COUNT("city") AS "Number of Schools in each city" FROM "schools"
WHERE "type" = 'Public School'
GROUP BY "city"
ORDER BY "Number of Schools in each city" DESC, "city"
LIMIT 10;
