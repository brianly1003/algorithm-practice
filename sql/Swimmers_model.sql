Write SQL Query:

Data Model:
-----------------------------------------
|	swimmers							|
-----------------------------------------
|	id					integer			|
|	name				varchar(50)		|
|	age					integer			|
|_______________________________________|

-----------------------------------------
|	events								|
-----------------------------------------
|	id					integer			|
|	event				varchar(50)		|
|	year				integer			|
|	gold				varchar(50)		|
|	silver				varchar(50)		|
|	bronze				varchar(50)		|
|_______________________________________|

Note: gold, silver, and bronze contain the names of athletes who have won medals in the event. 


########## 38. Exclusions in the JOIN ##########
Goal
Write a query that returns the number of gold medals per swimmer, for swimmers who received only gold medals. This means that the swimmers name will appear in the gold column of the events table, but not in the silver or bronze columns.

Requirements
1. Expected columns: name, total, in that order.
2. Sort the rows by name ascending.

Example:
---------------------------
| NAME            | TOTAL |
---------------------------
| Matthew Mccray  | 1     |
| Nicole Goldman  | 2     |
| Thomas Baker    | 11    |
---------------------------

QUERY:

SELECT s.name, COUNT(*) AS total
FROM swimmers s
INNER JOIN events e ON s.name = e.gold
LEFT JOIN events e1 ON s.name = e1.silver
LEFT JOIN events e2 ON s.name = e2.bronze
WHERE e1.id IS NULL AND e2.id IS NULL
GROUP BY s.name
ORDER BY s.name ASC


########## 48. Multiple CAST() and JOIN ##########
Goal
Write a query that returns the average age of gold, silver, and bronze medalists for each event. The average should be displayed as an integer (roundest to the nearest integer). 

Requirements
1. Expected columns: event, avg_age_gold, avg_age_silver, avg_age_bronze in that order.
2. Sort the rows by event ascending.

Example:
-----------------------------------------------------------------
| EVENT        | AVG_AGE_GOLD | AVG_AGE_SILVER | AVG_AGE_BRONZE |
-----------------------------------------------------------------
| 100m         | 23           | 24             | 25             |
| 1500m        | 25           | 25             | 24             |
| 200m         | 24           | 24             | 24             |
-----------------------------------------------------------------

QUERY:
SELECT e.event, 
    CAST(AVG(CAST(s1.age AS FLOAT)) AS INTEGER) AS AVG_AGE_GOLD, 
    CAST(AVG(CAST(s2.age AS FLOAT)) AS INTEGER) AS AVG_AGE_SILVER, 
    CAST(AVG(CAST(s3.age AS FLOAT)) AS INTEGER) AS AVG_AGE_BRONZE 
FROM events e
    INNER JOIN swimmers s1 ON e.gold = s1.name 
    INNER JOIN swimmers s2 ON e.silver = s2.name 
    INNER JOIN swimmers s3 ON e.bronze = s3.name 
GROUP BY e.event 
ORDER BY e.event
