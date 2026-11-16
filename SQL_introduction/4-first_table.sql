-- Creates the table first_table in the current database without failing.
-- Create the table only if it is missing
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
