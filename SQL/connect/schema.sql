CREATE TABLE "users" (
    "first_name" TEXT NOT NULL,
    "last_name" TEXT,
    "username" TEXT,
    "password" TEXT NOT NULL,
    PRIMARY KEY("username")
);

CREATE TABLE "schools" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "type" TEXT NOT NULL,
    "city" TEXT NOT NULL,
    "state" TEXT NOT NULL,
    "year" INTEGER NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE "companies" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "industry" TEXT NOT NULL,
    "city" TEXT NOT NULL,
    "state" TEXT NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE "people_connections" (
    "user1" TEXT,
    "user2" TEXT,
    PRIMARY KEY("user1", "user2"),
    FOREIGN KEY("user1") REFERENCES "users"("username"),
    FOREIGN KEY("user2") REFERENCES "users"("username")
);

CREATE TABLE "school_connections" (
    "user" TEXT NOT NULL,
    "school_id" INTEGER NOT NULL,
    "start_date" DATE,
    "end_date" DATE,
    "degree" TEXT,
    FOREIGN KEY("user") REFERENCES "users"("username"),
    FOREIGN KEY("school_id") REFERENCES "schools"("id")
);

CREATE TABLE "company_connections" (
    "user" TEXT NOT NULL,
    "company_id" INTEGER NOT NULL,
    "start_date" DATE,
    "end_date" DATE,
    "title" TEXT,
    FOREIGN KEY("user") REFERENCES "users"("username"),
    FOREIGN KEY("company_id") REFERENCES "companies"("id")
);
