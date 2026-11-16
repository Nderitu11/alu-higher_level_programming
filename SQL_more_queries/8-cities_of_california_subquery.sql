-- Lists all the cities of California found in the database hbtn_0d_usa.
-- Get the cities whose state id matches California, using a subquery
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
