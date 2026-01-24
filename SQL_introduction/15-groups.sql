-- sql lsit same number of the records
SELECT score, COUNT(*) AS number 
FROM second_table 
GROUP BY score
ORDER BY number DESC;
