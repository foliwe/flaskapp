create database flaskapp;
use flaskapp;

CREATE TABLE student (
    full_name VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    email VARCHAR(100) NOT NULL,
    sex VARCHAR(10) NOT NULL,
    date_of_stated DATE NOT NULL,
    country VARCHAR(100) NOT NULL,
    contact_number VARCHAR(20) NOT NULL,
    it_knowledge VARCHAR(20) NOT NULL,
    comment TEXT
);
