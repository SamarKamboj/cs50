SELECT "districts"."name"
FROM "districts"
JOIN "expenditures" ON "districts"."id" = "expenditures"."district_id"
WHERE "expenditures"."pupils" IN (
    SELECT MIN("pupils")
    FROM "expenditures"
);
