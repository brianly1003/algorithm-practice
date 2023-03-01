
Data model:
---------------------------------
|	convoy  					            |
---------------------------------
|	shipment_id		integer		      |
|	shipper_id		integer		      |
|	date_time		char(10)	        |
|	pickup_state	char(2)		      |
|	dropoff_state	char(2)		      |
|_______________________________|


7. ########## Window functions ##########
Goal
You want to know the number of shipments for the months of January through April 2020. Write a query that returns the following columns, in that order:

1. lane, a string concatenation of pickup_state and dropoff_state separated by a '-' (ex: 'CA-WA')
2. calendar_month, the numeric month of the shipment (ex: '1' for January 2020)
3. monthly_shipments, the count of shipments for that month and lane
4. shipments_to_date, the rolling sum of all 2020 shipments for that lane (up to the current month)


Requirements
Sort the rows by lane ascending, then by calendar_month ascending.

Example:
------------------------------------------------------------------
| LANE  | CALENDAR_MONTH | MONTHLY_SHIPMENTS | SHIPMENTS_TO_DATE |
------------------------------------------------------------------
| OR-OR | 1              | 3                 | 3                 |
| OR-OR | 2              | 3                 | 6                 |
| OR-OR | 3              | 1                 | 7                 |
| OR-OR | 4              | 1                 | 8                 |
| OR-WA | 1              | 7                 | 7                 |
| OR-WA | 2              | 4                 | 11                |
| OR-WA | 3              | 4                 | 15                |
------------------------------------------------------------------


QUERY:


9. ############ SUM with totals ############
---------------------------------
|	convoy  					|
---------------------------------
|	shipment_id		integer		|
|	shipper_id		integer		|
|	date_time		char(10)	|
|	pickup_state	char(2)		|
|	dropoff_state	char(2)		|
|_______________________________|

Goal
You want to know the number of shipments for the months of January through April 2020. Write a query that returns the following columns, in that order:

1. lane, a string concatenation of pickup_state and dropoff_state separated by a '-' (ex: 'CA-WA')
2. calendar_month, the numeric month of the shipment (ex: '1' for January 2020)
3. monthly_shipments, the count of shipments for that month and lane
4. total, the count of shipments for that month (regardless of the lane)
 

Requirements
Sort the rows by calendar_month ascending, then by lane ascending.
Example:
------------------------------------------------------
| LANE  | CALENDAR_MONTH | MONTHLY_SHIPMENTS | TOTAL |
------------------------------------------------------
| WA-WA | 1              | 3                 | 32    |
| CA-CA | 2              | 2                 | 30    |
| WA-OR | 3              | 3                 | 17    |
------------------------------------------------------



26. ############ Subquery with ROUND() and CAST() ############

Goal
In this data set, there is one shipper who has picked up over 50% (strictly) of their shipments from a single state. 

Write a query that prints this specific shipper and pickup state, together with the rate for that pickup state.

The rate is defined as the number of shipments from the pickup state over the total shipments done by the shipper. 


Requirements
Expected columns: shipper_id, pickup_state, rate, in that order.
rate should be rounded to keep only two decimals. 
Example:
------------------------------------
| SHIPPER_ID | PICKUP_STATE | RATE |
------------------------------------
| shipper_8  | CA           | 0.73 |
------------------------------------

QUERY:
-- create a subquery to find the total shipments done by each shipper
WITH total_shipments AS (
  SELECT shipper_id, COUNT(*) AS total
  FROM convoy
  GROUP BY shipper_id
)

-- join the subquery with the original table and calculate the rate for each pickup state
SELECT c.shipper_id, c.pickup_state, ROUND(COUNT(*) * 1.0 / t.total, 2) AS rate
FROM convoy c
JOIN total_shipments t ON c.shipper_id = t.shipper_id
GROUP BY c.shipper_id, c.pickup_state

-- filter out the shippers who have picked up less than 50% of their shipments from a single state
HAVING ROUND(COUNT(*) * 1.0 / t.total, 2) > 0.5;



46. ############ CASE WHEN with a subquery ############
Goal
Write a query that returns the total shipments for each shipper. If the shipper has performed some shipments that were picked up or dropped off in CA, add _CA to the end of shipper_id. 

Requirements
Expected columns: shipper_id, total, in that order.
Sort the rows by total descending, then by shipper_id ascending.
Example:
------------------------
| SHIPPER_ID   | TOTAL |
------------------------
| shipper_1_CA | 18    |
| shipper_6_CA | 14    |
| shipper_9    | 2     |
------------------------

QUERY:

SELECT 
  CONCAT(c.shipper_id, CASE WHEN (
    SELECT COUNT(*) 
    FROM convoy c1
    WHERE c1.shipper_id = c.shipper_id 
    AND (c1.pickup_state = 'CA' OR c1.dropoff_state = 'CA')) > 0 THEN '_CA' ELSE '' END) AS shipper_id,
  COUNT(*) AS total
FROM convoy c
GROUP BY shipper_id
ORDER BY total DESC, shipper_id ASC



47. ############ COUNT() on a filtered table ############
Goal
Write a query that returns the total number of shipments (regardless of the pickup state) by shippers, but only for shippers that have made strictly more than 6 shipments picked up in WA. 

Requirements
1. Expected columns: shipper_id, total, in that order.
2. Sort the rows by total descending, then by shipper_id ascending.

Example:
----------------------
| SHIPPER_ID | TOTAL |
----------------------
| shipper_1  | 20    |
| shipper_2  | 14    |
----------------------

QUERY:
SELECT c.SHIPPER_ID, COUNT(*) AS TOTAL
FROM convoy c
WHERE c.SHIPPER_ID IN (
    SELECT c1.SHIPPER_ID
    FROM convoy c1
    WHERE c1.pickup_state = 'WA'
    GROUP BY c1.SHIPPER_ID
    HAVING COUNT(*) > 6
)
GROUP BY c.SHIPPER_ID
ORDER BY TOTAL DESC, c.SHIPPER_ID ASC