using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Solution
{

    public static int FindSmallestInterval(int[] numbers)
    {
        // Write your code here
        // To debug: Console.Error.WriteLine("Debug messages...");
        Array.Sort(numbers); // Sort the array in ascending order
        int smallestInterval = int.MaxValue; // Initialize the smallest interval to the largest possible value
        for (int i = 1; i < numbers.Length; i++)
        {
            int interval = numbers[i] - numbers[i - 1]; // Compute the interval between adjacent elements
            if (interval < smallestInterval)
            {
                smallestInterval = interval; // Update the smallest interval if a smaller interval is found
            }
        }
        return smallestInterval;
    }

    /* Ignore and do not change the code below */
    static void Main(string[] args)
    {
        string[] inputs;
        int n = int.Parse(Console.ReadLine());
        int[] numbers = new int[n];
        inputs = Console.ReadLine().Split(' ');
        for (int i = 0; i < n; i++)
        {
            numbers[i] = int.Parse(inputs[i]);
        }
        var stdtoutWriter = Console.Out;
        Console.SetOut(Console.Error);
        int res = FindSmallestInterval(numbers);
        Console.SetOut(stdtoutWriter);
        Console.WriteLine(res);
    }
    /* Ignore and do not change the code above */
}