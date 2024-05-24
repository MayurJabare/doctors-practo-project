-- Connect to the database
-- (Assuming a PostgreSQL database, replace connection details as needed)

-- You can use a tool like pgAdmin or psql command-line interface to run these commands

-- Create a new database (optional)
CREATE DATABASE doctors_db;

-- Connect to the database (not necessary if you are already connected)
\c doctor_db;

-- Create the table with column name fetched from scrapping
CREATE TABLE doctor_info (
    id SERIAL PRIMARY KEY,
    doctor_name VARCHAR(255) NOT NULL,
    specialty VARCHAR(255),
    experience VARCHAR(255),
    locality VARCHAR(255),
    city VARCHAR(255),
    clinic_name VARCHAR(255),
    consultation_fee VARCHAR(255),
    recommendation VARCHAR(255),
    patient_stories VARCHAR(255)
);
