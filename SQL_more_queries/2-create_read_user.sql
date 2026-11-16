-- Creates the database hbtn_0d_2 and the user user_0d_2 with read access only.
-- Create the database only if it is missing
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create the user only if it is missing
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Give the user only the SELECT privilege on hbtn_0d_2
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
