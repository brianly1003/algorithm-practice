using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Solution
{
    public static int CalculateTotalPrice(int[] prices, int discount)
    {
        // Find the index of the most expensive item
        int maxIndex = 0;
        for (int i = 1; i < prices.Length; i++)
        {
            if (prices[i] > prices[maxIndex])
            {
                maxIndex = i;
            }
        }

        // Apply the discount to the most expensive item
        int discountedPrice = prices[maxIndex] * (100 - discount) / 100;

        // Compute the total purchase price
        int totalPrice = 0;
        for (int i = 0; i < prices.Length; i++)
        {
            if (i == maxIndex)
            {
                totalPrice += discountedPrice;
            }
            else
            {
                totalPrice += prices[i];
            }
        }

        // Return the total purchase price
        return totalPrice;
    }

    /* Ignore and do not change the code below */
    static void Main(string[] args)
    {
        string[] inputs;
        int discount = int.Parse(Console.ReadLine());
        int n = int.Parse(Console.ReadLine());
        int[] prices = new int[n];
        inputs = Console.ReadLine().Split(' ');
        for (int i = 0; i < n; i++)
        {
            prices[i] = int.Parse(inputs[i]);
        }
        var stdtoutWriter = Console.Out;
        Console.SetOut(Console.Error);
        int price = CalculateTotalPrice(prices, discount);
        Console.SetOut(stdtoutWriter);
        Console.WriteLine(price);
    }
    /* Ignore and do not change the code above */
}