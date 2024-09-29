-- Find public schools with their graduation and drop rates
-- having more than average graduation rate and less than average drop rate
-- sorted first by graduation rate (high-low) then by drop rate (low-high)

SELECT "schools"."name", "graduation_rates"."graduated", "graduation_rates"."dropped" FROM "schools"
JOIN "graduation_rates" ON "schools"."id" = "graduation_rates"."school_id"
WHERE "schools"."type" = 'Public School' AND "graduation_rates"."graduated" > (
    SELECT AVG("graduated") FROM "graduation_rates"
) AND "graduation_rates"."dropped" < (
    SELECT AVG("dropped") FROM "graduation_rates"
)
ORDER BY "graduation_rates"."graduated" DESC, "graduation_rates"."dropped";
