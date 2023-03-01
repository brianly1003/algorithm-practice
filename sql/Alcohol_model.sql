Write SQL Query:

Data Model:
-----------------------------------------
|	alcohol_consumption					|
-----------------------------------------
|	id					integer			|
|	country				varchar(50)		|
|	beer_consumption	integer			|
|	spirit_consumption	integer			|
|	wine_consumption	integer			|
|	total_consumption	float			|
|_______________________________________|


########## 33. Simple WHERE condition (inequality with calculated field) ##########
Goal
Write a query that returns all countries whose beer_consumption is strictly greater than their cumulated spirit_consumption and wine_consumption.

Requirements
Expected columns: country, beer_consumption, in that order.
Sort the rows by country ascending.
Example:
-----------------------------------------------
| COUNTRY                  | BEER_CONSUMPTION |
-----------------------------------------------
| Algeria                  | 25               |
| Burundi                  | 88               |
| Ecuador                  | 162              |
-----------------------------------------------
 

QUERY:
SELECT country, beer_consumption
FROM alcohol_consumption
WHERE beer_consumption > (spirit_consumption + wine_consumption)
ORDER BY country ASC;