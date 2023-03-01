using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Solution
{

    public static int[] CountFrequencies(string[] words)
    {
        // Create a dictionary to store the word frequencies
        Dictionary<string, int> freqs = new Dictionary<string, int>();

        // Iterate through the words and update the dictionary
        foreach (string word in words)
        {
            if (freqs.ContainsKey(word))
            {
                freqs[word]++;
            }
            else
            {
                freqs[word] = 1;
            }
        }

        // Sort the dictionary by key and convert to array
        int[] result = freqs.OrderBy(pair => pair.Key)
                            .Select(pair => pair.Value)
                            .ToArray();

        return result;
    }

    /* Ignore and do not change the code below */
    static void Main(string[] args)
    {
        string[] inputs;
        int n = int.Parse(Console.ReadLine());
        int x = int.Parse(Console.ReadLine());
        string[] words = new string[n];
        for (int i = 0; i < n; i++)
        {
            words[i] = Console.ReadLine();
        }
        var stdtoutWriter = Console.Out;
        Console.SetOut(Console.Error);
        int[] counts = CountFrequencies(words);
        Console.SetOut(stdtoutWriter);
        for (int i = 0; i < x; i++)
        {
            Console.WriteLine(counts[i]);
        }
    }
    /* Ignore and do not change the code above */
}