Data Model:
---------------------------------
|	location  					|
---------------------------------
|	location_id	integer			|
|	city		varchar(50)		|
|	state_provice	varchar(50)	|
|	postal_code		varchar(5)	|
|	country			varchar(20)	|
|_______________________________|


-----------------------------------------
|	vehicle_part_location				|
-----------------------------------------
|	vehicle_part_location_id	integer	|
|	location_id					integer	|
|	vehicle_part_id				integer	|
|	postal_code		varchar(5)			|
|	country			varchar(20)			|
|_______________________________________|


-----------------------------------------
|	vehicle_part						|
-----------------------------------------
|	vehicle_part_id	integer				|
|	rfid			varchar(255)		|
|	purchase_price	decimal(25,5)		|
|	sold_price		decimal(25,5)		|
|	vehicle_id		integer				|
|	make			varchar(50)			|
|	model			varchar(50)			|
|	year			integer				|
|	part_name		varchar(50)			|
|_______________________________________|


-----------------------------------------
|	vehicle								|
-----------------------------------------
|	vehicle_id		integer				|
|	vehicle_name	varchar(50)			|
|	vin				varchar(50)			|
|	make			varchar(50)			|
|	model			varchar(50)			|
|	year			integer				|
|_______________________________________|

-----------------------------------------
|	vehicle_part_supplier				|
-----------------------------------------
|	supplier_id		integer				|
|	vehicle_part_id	integer				|
|_______________________________________|


-----------------------------------------
|	supplier							|
-----------------------------------------
|	supplier_id		integer				|
|	city			varchar(50)			|
|	state_provice	varchar(30)			|
|	postal_code		varchar(5)			|
|	country			varchar(20)			|
|	name			varchar(20)			|
|_______________________________________|


########## [Vehicle Data Model] Complext join #1: ##########
Goal
Extract the number of parts (vehicle_part) and suppliers (supplier) per vehicle, for vehicles with 2 or more suppliers. 

Requirements
Expected columns: vehicle_name, vehicle_part_count, supplier_count, in that order.

Example:
------------------------------------------------------
| VEHICLE_NAME | VEHICLE_PART_COUNT | SUPPLIER_COUNT |
------------------------------------------------------
| FJ6557       | 1                  | 3              |
| HKKY88       | 3                  | 6              |
------------------------------------------------------

QUERY:

SELECT v.vehicle_name, COUNT(DISTINCT vp.vehicle_part_id) AS vehicle_part_count, COUNT(DISTINCT s.supplier_id) AS supplier_count
FROM vehicle v
JOIN vehicle_part vp ON v.vehicle_id = vp.vehicle_id
JOIN vehicle_part_supplier vps ON vp.vehicle_part_id = vps.vehicle_part_id
JOIN supplier s ON vps.supplier_id = s.supplier_id
GROUP BY v.vehicle_name
HAVING COUNT(DISTINCT s.supplier_id) >= 2;


########## [Vehicle Data Model] Complext join #2: ##########
Goal
Extract the make and model of the vehicle(s) with the most vehicle parts.
 
Requirements
Expected columns: make, model, in that order.
Example:
-------------------
| MAKE   | MODEL  |
-------------------
| Ford   | F150   |
-------------------

QUERY:

SELECT	v.make, v.model
FROM	vehicle v
INNER JOIN vehicle_part vp ON v.vehicle_id = vp.vehicle_id
GROUP BY v.make, v.model
HAVING COUNT(vp.vehicle_part_id) = (
  SELECT MAX(part_count) 
  FROM (
    SELECT COUNT(vehicle_part_id) AS part_count
    FROM vehicle_part
    GROUP BY vehicle_id
  ) AS subquery
);



########## 50. [Vehicle Data Model] Aggregate: USING ALL() ##########
Goal
Extract the vehicle parts whose departure time (left_timestamp) is greater than all vehicle parts arrival times (arrived_timestamp).
 
Requirements
Expected columns: vehicle_part_id, part_name, left_timestamp, in that order.
Example: 
----------------------------------------------------------------
| VEHICLE_PART_ID | PART_NAME    | LEFT_TIMESTAMP              |
----------------------------------------------------------------
| 11              | Starter      | 2019-05-26T08:30:52.0000000 |
----------------------------------------------------------------


QUERY:

SELECT vp.VEHICLE_PART_ID, vp.PART_NAME, vpl.LEFT_TIMESTAMP
FROM vehicle_part vp
    INNER JOIN vehicle_part_location vpl on vpl.VEHICLE_PART_ID = vp.VEHICLE_PART_ID
WHERE vpl.LEFT_TIMESTAMP > ALL(
    SELECT vpl1.arrived_timestamp
    FROM vehicle_part_location vpl1
    WHERE vpl1.arrived_timestamp IS NOT NULL
)


########## 51. [Vehicle Data Model] SQL - Auto join ##########
Goal
Extract the ids of vehicles that have at least one location in common with the vehicle that has id 34.
 
Requirements
1. Expected column: vehicle_id.
2. The output should not contain any duplicates (or contain the id 34).

Example:
---------------
| VEHICLE_ID |
---------------
| 2           |
| 8           |
---------------

QUERY:

SELECT DISTINCT v.vehicle_id
FROM vehicle v
JOIN vehicle_part vp ON vp.vehicle_id = v.vehicle_id
JOIN vehicle_part_location vpl ON vpl.vehicle_part_id = vp.vehicle_part_id
JOIN (
    SELECT DISTINCT location_id
    FROM vehicle_part_location
    JOIN vehicle_part ON vehicle_part_location.vehicle_part_id = vehicle_part.vehicle_part_id
    WHERE vehicle_part.vehicle_id = 34
) subq ON subq.location_id = vpl.location_id
WHERE v.vehicle_id != 34;