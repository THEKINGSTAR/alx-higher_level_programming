-- a script that displays the max temperature of each state (ordered by State name).
SELECT temperatures.state, MAX(temperatures.value) AS max_temp
FROM temperatures
GROUP BY state;

