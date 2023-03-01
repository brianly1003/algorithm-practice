using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Solution
{

    public static int ComputeMultiplesSum(int n)
    {
        // Write your code here
        // To debug: Console.Error.WriteLine("Debug messages...");
        var sum = 0;

        for (var i = 1; i < n; i++) {
            if (i % 3 == 0 || i % 5 == 0 || i % 7 == 0) {
                sum += i;
            }
        }

        return sum;
    }

    /* Ignore and do not change the code below */
    static void Main(string[] args)
    {
        int n = int.Parse(Console.ReadLine());
        var stdtoutWriter = Console.Out;
        Console.SetOut(Console.Error);
        int res = ComputeMultiplesSum(n);
        Console.SetOut(stdtoutWriter);
        Console.WriteLine(res);
    }
    /* Ignore and do not change the code above */
}