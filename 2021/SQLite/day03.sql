-- SQLite
DROP TABLE IF EXISTS data;
CREATE TABLE data (
  x CHAR
);

.import /home/sudoku/Documents/Coding/AdventOfCode/2021/Data/day03 data

-- Part one
DROP TABLE IF EXISTS bins
CREATE TABLE bins AS
  SELECT
    SUBSTRING(x, 1, 1) AS a,
    SUBSTRING(x, 2, 1) AS b,
    SUBSTRING(x, 3, 1) AS c,
    SUBSTRING(x, 4, 1) AS d,
    SUBSTRING(x, 5, 1) AS e,
    SUBSTRING(x, 6, 1) AS f,
    SUBSTRING(x, 7, 1) AS g,
    SUBSTRING(x, 8, 1) AS h,
    SUBSTRING(x, 9, 1) AS i,
    SUBSTRING(x, 10, 1) AS j,
    SUBSTRING(x, 11, 1) AS k,
    SUBSTRING(x, 12, 1) AS l
  FROM data

DROP TABLE IF EXISTS gamma_rate
CREATE TABLE gamma_rate AS
  SELECT
    IIF(SUM(a)<500, 0 , 1) * POWER(2, 11) +
    IIF(SUM(b)<500, 0 , 1) * POWER(2, 10) +
    IIF(SUM(c)<500, 0 , 1) * POWER(2, 9) +
    IIF(SUM(d)<500, 0 , 1) * POWER(2, 8) +
    IIF(SUM(e)<500, 0 , 1) * POWER(2, 7) +
    IIF(SUM(f)<500, 0 , 1) * POWER(2, 6) +
    IIF(SUM(g)<500, 0 , 1) * POWER(2, 5) +
    IIF(SUM(h)<500, 0 , 1) * POWER(2, 4) +
    IIF(SUM(i)<500, 0 , 1) * POWER(2, 3) +
    IIF(SUM(j)<500, 0 , 1) * POWER(2, 2) +
    IIF(SUM(k)<500, 0 , 1) * POWER(2, 1) +
    IIF(SUM(l)<500, 0 , 1) * POWER(2, 0)
    AS gamma_rate
  FROM bins

WITH epsilon_rate AS
  (
  SELECT POWER(2, 12) - 1 - gamma_rate AS epsilon_rate
  FROM gamma_rate
  )
SELECT
  CAST
  (
  gamma_rate * epsilon_rate AS INT
  ) AS powerconsumption
FROM gamma_rate, epsilon_rate


-- Part two
-- WITH oxygen_generator_rating AS
--   (
--     SELECT *
--     FROM bins
--     WHERE a = (SELECT CAST(ROUND(AVG(a)) AS INT) FROM bins)
--   )

-- DROP TABLE IF EXISTS oxygen_generator_rating

CREATE TABLE IF NOT EXISTS oxygen_generator_rating AS (
  SELECT * 
  FROM bins
  WHERE a = (
    SELECT 
      CAST(ROUND(AVG(a)) AS INT) 
    FROM bins
  )
)


SELECT * FROM oxygen_generator_rating

-- DELETE FROM oxygen_generator_rating
-- WHERE b != (SELECT CAST(ROUND(AVG(b)) AS INT) FROM bins)

