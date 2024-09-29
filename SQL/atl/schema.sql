CREATE TABLE "passengers"(
    "id" INTEGER,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT,
    "age" INTEGER NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE "airlines"(
    "id" INTEGER,
    "name" TEXT NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE "concourses"(
    "id" INTEGER,
    "name" TEXT NOT NULL CHECK("name" IN ('A', 'B', 'C', 'D', 'E', 'F', 'T')),
    PRIMARY KEY("id")
);

CREATE TABLE "airline_concourse"(
    "airline_id" INTEGER,
    "concourse_id" INTEGER,
    PRIMARY KEY("airline_id", "concourse_id"),
    FOREIGN KEY("airline_id") REFERENCES "airlines"("id"),
    FOREIGN KEY("concourse_id") REFERENCES "concourses"("id")
);

CREATE TABLE "flights"(
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "airline_id" INTEGER,
    "departure_airport" TEXT NOT NULL,
    "departure_date" DATE NOT NULL,
    "departure_time" TIME NOT NULL,
    "arrival_airport" TEXT NOT NULL,
    "arrival_date" DATE NOT NULL,
    "arrival_time" TIME NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY("airline_id") REFERENCES "airlines"("id")
);

CREATE TABLE "check_ins"(
    "id" INTEGER,
    "passenger_id" INTEGER NOT NULL,
    "flight_id" INTEGER NOT NULL,
    "date" DATE NOT NULL,
    "time" TIME NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY("passenger_id") REFERENCES "passengers"("id"),
    FOREIGN KEY("flight_id") REFERENCES "flights"("id")
);
