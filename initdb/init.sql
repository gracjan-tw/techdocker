CREATE USER pingStats WITH PASSWORD 'pingStats';
CREATE DATABASE pingStats OWNER pingStats;

CREATE TABLE uptime (
    "when" TIMESTAMPTZ,
    who TEXT,
    value INT
);
