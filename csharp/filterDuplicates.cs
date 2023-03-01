using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Solution
{

    public static int[] FilterDuplicates(int[] data)
    {
        HashSet<int> set = new HashSet<int>();
        List<int> result = new List<int>();

        foreach (int val in data)
        {
            if (!set.Contains(val))
            {
                set.Add(val);
                result.Add(val);
            }
        }

        return result.ToArray();
    }

    /* Ignore and do not change the code below */
    static void Main(string[] args)
    {
        string[] inputs;
        int n = int.Parse(Console.ReadLine());
        int[] data = new int[n];
        inputs = Console.ReadLine().Split(' ');
        for (int i = 0; i < n; i++)
        {
            data[i] = int.Parse(inputs[i]);
        }
        var stdtoutWriter = Console.Out;
        Console.SetOut(Console.Error);
        int[] filtered = FilterDuplicates(data);
        Console.SetOut(stdtoutWriter);
        for (int i = 0; i < filtered.GetLength(0); i++)
        {
            Console.WriteLine(filtered[i]);
        }
    }
    /* Ignore and do not change the code above */
}