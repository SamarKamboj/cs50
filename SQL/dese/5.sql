SELECT "city", COUNT("name") AS "Number of Schools in each city" FROM "schools"
WHERE "type" = 'Public School'
GROUP BY "city"
HAVING "Number of Schools in each city" <= 3
ORDER BY "Number of Schools in each city" DESC, "city";
