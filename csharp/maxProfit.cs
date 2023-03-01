using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Runtime.Serialization;

public class Solution
{

    public static List<int> MaxProfit(List<int> data)
    {
        // Write your code here
        int maxEndingHere = data[0];
        int maxSoFar = data[0];
        int start = 0;
        int end = 0;
        int currentStart = 0;

        for (int i = 1; i < data.Count; i++)
        {
            if (data[i] > data[i] + maxEndingHere)
            {
                maxEndingHere = data[i];
                currentStart = i;
            }
            else
            {
                maxEndingHere += data[i];
            }

            if (maxEndingHere > maxSoFar)
            {
                maxSoFar = maxEndingHere;
                start = currentStart;
                end = i;
            }
        }

        return new List<int>() { start, end };
    }

    /* Ignore and do not change the code below */

    /**
     * Try a solution
     */
    private static void TrySolution(List<int> months)
    {
        Console.WriteLine("" + JsonSerializer.Serialize(months));
    }

    public static void Main(string[] args)
    {
        TrySolution(MaxProfit(
            JsonSerializer.Deserialize<List<int>>(Console.ReadLine())
        ));
    }
    /* Ignore and do not change the code above */
}


