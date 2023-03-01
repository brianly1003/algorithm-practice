/* Objective
Suppose there is a sale on blue, green, and red shirts for the next n days. On day 
, it costs 
 dollars to buy a blue shirt, 
 dollars to buy a green shirt, and 
 dollars to buy a red shirt. You wish to buy a single shirt for each for the next n days, but with the caveat that you cannot buy the same color shirt on consecutive days.

 
Implementation
Implement the method LowestCost(blueCosts, greenCosts, redCosts) which takes in three lists of length n: blueCosts, greenCosts, redCosts. Each element in these lists is a positive integer that represents the daily price of a shirt. 

Your task is to output a list representing the shirt color you buy for each of the n days, such that the total combined cost of the n shirts is minimized. Specifically, your output list will be of length n, where each element in the list is either 'b', 'g', or 'r'. The 
 element of the output list represents the color of the 
 day's shirt. Note that there will be exactly one color sequence that minimizes the cost for the n shirts.

 
Examples
For inputs

blueCosts = [1, 1, 1]
greenCosts = [3, 5, 7]
redCosts = [4, 6, 4]
the output list should be ['b', 'g', 'b'] (total cost of 7). Buying only blue shirts would be the cheapest, but remember that no two consecutive days can have the same color shirt.

 
For inputs

blueCosts = [18, 12, 1, 9]
greenCosts = [13, 15, 7, 9]
redCosts = [12, 16, 4, 8]
the output list should be ['r', 'g', 'b', 'r'] (total cost of 36).

 
For inputs

blueCosts = [100, 1, 76, 14]
greenCosts = [22, 20, 1, 2]
redCosts = [99, 99, 5, 12]
the output list should be ['g', 'b', 'r', 'g'] (total cost of 30).

  */