-- SQLite
DROP TABLE IF EXISTS data;
CREATE TABLE data (
  d VARCHAR,
  x INTEGER,
  id INTEGER PRIMARY KEY AUTOINCREMENT
);

.separator ' '
.import /home/sudoku/Documents/Coding/AdventOfCode/2021/Data/day02 data

-- Part one
SELECT forward * (down - up)
FROM 
  (SELECT SUM(x) AS forward FROM data WHERE data.d like 'forward'),
  (SELECT SUM(x) AS up FROM data WHERE data.d like 'up'),
  (SELECT SUM(x) AS down from data WHERE data.d like 'down');

-- Part two
SELECT horizontal * SUM(depth)
FROM 
  (
    SELECT 
    (
      SELECT (down - up)
      FROM
      ( 
        SELECT SUM(x) AS up
        FROM data 
        WHERE data.d LIKE 'up' 
        AND data.id <= data2.id
      ),
      (
        SELECT SUM(x) AS down 
        FROM data 
        WHERE data.d LIKE 'down' 
        AND data.id <= data2.id
      )
    ) * x AS depth
    FROM data AS data2
    WHERE data2.d LIKE 'forward'
  ),
  (
  SELECT SUM(x) AS horizontal 
  FROM data 
  WHERE data.d LIKE 'forward'
);