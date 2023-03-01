/* 
* Objective
* In this problem, you'll be given a list of positive integers and a separate integer, k, 
* and tasked with finding whether there is a pair of integers in the list that sum to exactly k.

* Implementation
* Implement the method FindSumPair(numbers, k) which takes as input:

* an array of positive integers (numbers).
* a positive integer (k), representing the target sum. 
* For example:
* numbers = [1, 5, 8, 1, 2]
* k = 13
 
* Your FindSumPair method should return an array of two integers, containing the indices of a pair of integers in the array that sum to k. Note that:
* The first index of the array is 0. 
* The first integer in your output should represent the lower index. 
* [0, 0] should be returned if there no pair is found. 
* In the case that there are multiple possible pairs that sum to the target, return the pair whose left index is the lowest.
* In the case of two pairs having the same left index, favor the pair with the lower right index.
 
* For the above example, the correct output would be: [1, 2]. 
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Solution
{
    public static int[] FindSumPair(int[] numbers, int k)
    {
        var dicts = new Dictionary<int, int>();

        for (var i = 0; i < numbers.Length; i++)
        {
            var complement = k - numbers[i];
            if (dicts.ContainsKey(complement))
            {
                return new[] { dicts[complement], i };
            }
            else if (!dicts.ContainsKey(numbers[i]))
            {
                dicts[numbers[i]] = i;
            }
        }

        return new[] { 0, 0 };
    }


    public static int[] FindSumPair2(int[] numbers, int k)
    {
        var indices = new Dictionary<int, int>();
        var lowestLeft = int.MaxValue;
        var lowestRight = int.MaxValue;

        for (int i = 0; i < numbers.Length; i++)
        {
            int complement = k - numbers[i];
            if (indices.ContainsKey(complement))
            {
                int left = Math.Min(i, indices[complement]);
                int right = Math.Max(i, indices[complement]);

                if (left < lowestLeft)
                {
                    lowestLeft = left;
                    lowestRight = right;
                }
                else if (left == lowestLeft && right < lowestRight)
                {
                    lowestRight = right;
                }
            }
            else
            {
                indices[numbers[i]] = i;
            }
        }

        if (lowestLeft == int.MaxValue)
        {
            return new int[] { 0, 0 };
        }
        else
        {
            return new int[] { lowestLeft, lowestRight };
        }
    }
}