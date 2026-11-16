-- Creates the table force_name where name cannot be null.
-- Create the table only if it is missing
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
