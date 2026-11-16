-- Creates the MySQL user user_0d_1 with all privileges on the server.
-- Create the user only if it is missing
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Give the user every privilege on every database
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
