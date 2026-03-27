-- [Week 10 Friday Lab] 
-- Database Setup for Final Project

DROP TABLE IF EXISTS observations;

CREATE TABLE observations(
    id SERIAL PRIMARY KEY,
    city VARCHAR(100),
    country VARCHAR(10),
    latitude DECIMAL,
    longitude DECIMAL,
    temperature_c DECIMAL,
    windspeed_kmh DECIMAL,
    observation_time TIMESTAMP,
    notes TEXT
);

SELECT * FROM observations;

SELECT * FROM observations WHERE id = 1;

SELECT AVG(temperature_c) AS avg_temp, 
    MAX(windspeed_kmh) AS max_wind
FROM observations;