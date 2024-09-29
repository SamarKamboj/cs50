INSERT INTO "users"
VALUES ('Alan', 'Garber', 'alan', 'password'), ('Reid', 'Hoffman', 'reid', 'password');

INSERT INTO "schools" ("name", "type", "city", "state", "year")
VALUES ('Harvard University', 'University', 'Cambridge', 'Massachusetts', 1636);

INSERT INTO "companies" ("name", "industry", "city", "state")
VALUES ('LinkedIn', 'Technology', 'Sunnyvale', 'California');

INSERT INTO "school_connections"
VALUES (
    (SELECT "username" FROM "users" WHERE "first_name" = 'Alan' AND "last_name" = 'Garber'),
    (SELECT "id" FROM "schools" WHERE "name" = 'Harvard University'),
    '1973-09-01',
    '1976-06-01',
    'BA'
);

INSERT INTO "company_connections"
VALUES (
    (SELECT "username" FROM "users" WHERE "first_name" = 'Reid' AND "last_name" = 'Hoffman'),
    (SELECT "id" FROM "companies" WHERE "name" = 'LinkedIn'),
    '2003-01-01',
    '2007-02-01',
    'CEO'
);
