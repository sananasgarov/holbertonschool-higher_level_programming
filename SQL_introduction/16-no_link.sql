-- sql lsit same number of the records
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
