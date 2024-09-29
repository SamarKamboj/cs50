INSERT INTO "ingredients" ("name", "price_per_unit", "unit")
VALUES ('Cocoa', 5, 'pound'), ('Sugar', 2, 'pound'), ('Buttermilk', NULL, NULL), ('Flour', NULL, NULL), ('Sprinkles', NULL, NULL);

INSERT INTO "donuts" ("name", "is_gluten-free", "price")
VALUES ('Belgian Dark Chocolate', 'No', 4), ('Back-To-School Sprinkles', 'No', 4);

INSERT INTO "ingredients_in_donut" ("donut_id", "ingredient_id")
VALUES (
    (SELECT "id" FROM "donuts" WHERE "name" = 'Belgian Dark Chocolate'),
    (SELECT "id" FROM "ingredients" WHERE "name" = 'Cocoa')
),
(
    (SELECT "id" FROM "donuts" WHERE "name" = 'Belgian Dark Chocolate'),
    (SELECT "id" FROM "ingredients" WHERE "name" = 'Flour')
),
(
    (SELECT "id" FROM "donuts" WHERE "name" = 'Belgian Dark Chocolate'),
    (SELECT "id" FROM "ingredients" WHERE "name" = 'Buttermilk')
),
(
    (SELECT "id" FROM "donuts" WHERE "name" = 'Belgian Dark Chocolate'),
    (SELECT "id" FROM "ingredients" WHERE "name" = 'Sugar')
);

INSERT INTO "customers" ("name")
VALUES ('Luis Singh');

INSERT INTO "orders" ("customer_id")
VALUES (
    (SELECT "id" FROM "customers" WHERE "name" = 'Luis Singh')
);

INSERT INTO "order_details"
VALUES (
    1,
    (SELECT "id" FROM "donuts" WHERE "name" = 'Back-To-School Sprinkles'),
    2
),
(
     1,
     (SELECT "id" FROM "donuts" WHERE "name" = 'Belgian Dark Chocolate'),
     3
);
