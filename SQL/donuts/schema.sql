CREATE TABLE "ingredients" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "price_per_unit" INTEGER,
    "unit" TEXT,
    PRIMARY KEY("id")
);

CREATE TABLE "donuts" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "is_gluten-free" TEXT,
    "price" INTEGER NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE "ingredients_in_donut" (
    "donut_id" INTEGER NOT NULL,
    "ingredient_id" INTEGER NOT NULL,
    PRIMARY KEY("donut_id", "ingredient_id"),
    FOREIGN KEY("donut_id") REFERENCES "donuts"("id"),
    FOREIGN KEY("ingredient_id") REFERENCES "ingredients"("id")
);

CREATE TABLE "customers" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE "orders" (
    "id" INTEGER,
    "customer_id" INTEGER,
    "time" DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY("id"),
    FOREIGN KEY("customer_id") REFERENCES "customers"("id")
);

CREATE TABLE "order_details"(
    "order_id" INTEGER NOT NULL,
    "donut_id" INTEGER NOT NULL,
    "quantity" INTEGER,
    PRIMARY KEY("order_id", "donut_id"),
    FOREIGN KEY("order_id") REFERENCES "orders"("id"),
    FOREIGN KEY("donut_id") REFERENCES "donuts"("id")
);

