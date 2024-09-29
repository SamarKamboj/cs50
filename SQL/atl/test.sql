INSERT INTO "passengers" ("first_name", "last_name", "age")
VALUES ('Amelia', 'Earhart', 39);

INSERT INTO "airlines" ("name")
VALUES ('Delta');

INSERT INTO "concourses" ("name")
VALUES ('A'), ('B'), ('C'), ('D'), ('T');

INSERT INTO "airline_concourse" ("airline_id", "concourse_id")
VALUES ((SELECT "id" FROM "airlines" WHERE "name" = 'Delta'), (SELECT "id" FROM "concourses" WHERE "name" = 'A')),
((SELECT "id" FROM "airlines" WHERE "name" = 'Delta'), (SELECT "id" FROM "concourses" WHERE "name" = 'B')),
((SELECT "id" FROM "airlines" WHERE "name" = 'Delta'), (SELECT "id" FROM "concourses" WHERE "name" = 'C')),
((SELECT "id" FROM "airlines" WHERE "name" = 'Delta'), (SELECT "id" FROM "concourses" WHERE "name" = 'D')),
((SELECT "id" FROM "airlines" WHERE "name" = 'Delta'), (SELECT "id" FROM "concourses" WHERE "name" = 'T'));

INSERT INTO "flights" (
    "name",
    "airline_id",
    "departure_airport",
    "departure_date",
    "departure_time",
    "arrival_airport",
    "arrival_date",
    "arrival_time"
)
VALUES (
    'Delta Flight 300',
    (SELECT "id" FROM "airlines" WHERE "name" = 'Delta'),
    'ATL',
    '2023-08-03',
    '18:46',
    'BOS',
    '2023-08-03',
    '21:09'
);

INSERT INTO "check_ins" ("passenger_id", "flight_id", "date", "time")
VALUES (
    (SELECT "id" FROM "passengers" WHERE "first_name" = 'Amelia' AND "last_name" = 'Earhart' AND "age" = 39),
    (SELECT "id" FROM "flights" WHERE "name" = 'Delta Flight 300'),
    '2023-08-03',
    '15:03'
);
