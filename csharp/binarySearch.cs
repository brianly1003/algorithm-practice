
// C# code below
using System;
using System.IO;


// TODO: Approach 1: Using Array.BinarySearch() function
// TODO: Approach 2: Write a binary search function

public class Answer
{
    public static bool Exists(int[] ints, int k)
    {
        var result = Array.BinarySearch(ints, value: k);
        return result >= 0;
    }

    public static bool Exists2(int[] ints, int k)
    {
        var left = 0;
        var right = ints.Length - 1;

        while (left <= right)
        {
            //? https://stackoverflow.com/questions/6735259/calculating-mid-in-binary-search
            //? int mid = left + (right - left) / 2;
            int mid = (low + high) >> 1;

            if (ints[mid] == k)
            {
                return true;
            }
            else if (ints[mid] < k)
            {
                left = mid + 1;
            }
            else
            {
                right = mid - 1;
            }
        }

        return false;
    }
}

/*
*    The aim of this exercise is to check the presence of a number in an array.

*   Specifications:
*    The items are integers arranged in ascending order.
*    The array can contain up to 1 million items
*    The array is never null
*    Implement the method boolean Answer.Exists(int[] ints, int k) so that it returns true if k belongs to ints, otherwise the method should return false.

*   Important note: Try to save CPU cycles if possible.

*   Example:
*    int[] ints = {-9, 14, 37, 102};
*    Answer.Exists(ints, 102) returns true
*    Answer.Exists(ints, 36) returns false
*/