using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Solution
{

    public static string IsDuoDigit(int number)
    {
        // Write your code here
        // To debug: Console.Error.WriteLine("Debug messages...");

        string digits = Math.Abs(number).ToString();
        if (digits.Length <= 2)
        {
            return "y";
        }
        else if (digits.Distinct().Count() <= 2)
        {
            return "y";
        }
        else
        {
            return "n";
        }
    }

    /* Ignore and do not change the code below */
    static void Main(string[] args)
    {
        int number = int.Parse(Console.ReadLine());
        var stdtoutWriter = Console.Out;
        Console.SetOut(Console.Error);
        string result = IsDuoDigit(number);
        Console.SetOut(stdtoutWriter);
        Console.WriteLine(result);
    }
    /* Ignore and do not change the code above */
}