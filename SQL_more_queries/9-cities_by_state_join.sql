-- Lists all cities of hbtn_0d_usa with the name of their state.
-- Get city id, city name and state name, ordered by city id
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
