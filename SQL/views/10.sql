-- Average brightness of 10 prints having least contrast by Hokusai
SELECT ROUND(AVG(brightness), 2) AS "Average Brightness" FROM (SELECT brightness FROM views WHERE artist = "Hokusai" ORDER BY contrast LIMIT 10);
