
<!-- https://www.youtube.com/watch?v=4SNzC4uNmTA&t=67s -->
## Construction of Binary Indexed Tree
+ Binary Indexed Tree (BIT) is an array in which each node stores sum of some elements of a given array for which the BI Tree is made...
+ Size of Binary Indexed Tree is equal to N where N is size of input array.
+ It takes O(LogN) time for both operations i.e to find sum of first i elements & update value of a specified element.

BI Tree for an array arr[] has following operations:
1. update(): Updates BI Tree for operation arr[index] += val
2. getSum(): Returns sum of arr[0...index]

We first initialize all values in BITree[] as 0.
Then we call update() operation for all indexes to insert values according to given array.


