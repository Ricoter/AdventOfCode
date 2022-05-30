-- SQLite
DROP TABLE IF EXISTS day01;
CREATE TABLE day01 (
  x INTEGER,
  id INTEGER PRIMARY KEY AUTOINCREMENT
);

.import /home/sudoku/Documents/Coding/AdventOfCode/2021/Data/day01 day01

-- Part one
SELECT COUNT(*)
FROM (
  (SELECT * FROM day01) AS a
  JOIN
  (SELECT * FROM day01) AS b
  ON a.id = b.id - 1
) WHERE a.x < b.x

-- Part two
SELECT COUNT(*)
FROM (
  (SELECT * FROM day01) a
  JOIN
  (SELECT * FROM day01) b
  ON a.id = b.id - 1
  JOIN
  (SELECT * FROM day01) c
  ON a.id = c.id - 2
  JOIN
  (SELECT * FROM day01) d
  ON a.id = d.id - 3
) WHERE (a.x + b.x + c.x) < (b.x + c.x + d.x)