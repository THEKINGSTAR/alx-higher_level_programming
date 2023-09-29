-- a script that displays the top 3 of cities temperature
-- during July and August ordered by temperature (descending)
SELECT temperatures.city, avg(temperatures.value) AS avg_temp
FROM temperatures
WHERE temperatures.month IN ('July', 'August')
GROUP BY city
ORDER BY avg_temp DESC LIMIT 3;
