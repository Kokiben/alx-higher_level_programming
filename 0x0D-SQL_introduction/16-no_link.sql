-- list all records of the table second_table
-- record are ordered by score.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
