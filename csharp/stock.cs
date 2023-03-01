using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Solution
{

    public static string[] GetTopStocks(string[] stocks, float[,] prices)
    {
        var stockAverages = new Dictionary<string, float>();
        for (int i = 0; i < stocks.Length; i++)
        {
            float sum = 0;
            for (int j = 0; j < prices.GetLength(0); j++)
            {
                // Console.Error.WriteLine($"{j} - {i} - {prices[j, i]}");
                sum += prices[j, i];
            }

            // Console.Error.WriteLine(prices.GetLength(0));
            float average = sum / prices.GetLength(0);
            stockAverages[stocks[i]] = average;
        }

        // Sort the stocks by decreasing average price and return the top three
        return stockAverages.OrderByDescending(kv => kv.Value)
                           .Take(3)
                           .Select(kv => kv.Key)
                           .ToArray();
    }

    /* Ignore and do not change the code below */
    static void Main(string[] args)
    {
        string[] inputs;
        int nbstocks = int.Parse(Console.ReadLine());
        int nbdays = int.Parse(Console.ReadLine());
        string[] stocks = new string[nbstocks];
        for (int i = 0; i < nbstocks; i++)
        {
            stocks[i] = Console.ReadLine();
        }
        float[,] prices = new float[nbdays, nbstocks];
        for (int i = 0; i < nbdays; i++)
        {
            inputs = Console.ReadLine().Split(' ');
            for (int j = 0; j < nbstocks; j++)
            {
                prices[i, j] = float.Parse(inputs[j]);
            }
        }
        var stdtoutWriter = Console.Out;
        Console.SetOut(Console.Error);
        string[] top = GetTopStocks(stocks, prices);
        Console.SetOut(stdtoutWriter);
        for (int i = 0; i < 3; i++)
        {
            Console.WriteLine(top[i]);
        }
    }
    /* Ignore and do not change the code above */
}


/*
* Objective
* In this problem, you'll be given a list of daily stock prices, and you'll be asked to return the three stocks with the highest average price.

 
* Implementation
* Implement the method GetTopStocks(stocks, prices) which takes as input:

* an array of strings (stocks), representing the considered stocks.
* an array of 2 dimensions (prices), representing the stock prices (inner lists) for each day (outer list). 
* An example input would look like this:

*   ['AMZN', 'CACC', 'EQIX', 'GOOG', 'ORLY', 'ULTA']
*   [
*       [12.81, 11.09, 12.11, 10.93, 9.83, 8.14],   day-1
*       [10.34, 10.56, 10.14, 12.17, 13.1, 11.22],  day-2
*       [11.53, 10.67, 10.42, 11.88, 11.77, 10.21]  day-3
*   ]
 
* Your GetTopStocks method should return an array containing the names of the three stocks with the highest average value. The array should be sorted by decreasing average value. You're guaranteed that each stock will have a unique average value.

* For the above example, the correct output would be:
* ['GOOG', 'ORLY', 'AMZN'] */