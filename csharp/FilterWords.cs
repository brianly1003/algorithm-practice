using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Solution
{
    public static string[] FilterWords(string[] words, string letters)
    {
        HashSet<char> letterSet = new HashSet<char>(letters);
        List<string> filteredWords = new List<string>();
        foreach (string word in words)
        {
            foreach (char letter in word)
            {
                if (letterSet.Contains(letter))
                {
                    filteredWords.Add(word);
                    break;
                }
            }
        }
        return filteredWords.ToArray();
    }

    /* Ignore and do not change the code below */
    static void Main(string[] args)
    {
        string[] inputs;
        int n = int.Parse(Console.ReadLine());
        string[] words = new string[n];
        for (int i = 0; i < n; i++)
        {
            words[i] = Console.ReadLine();
        }
        string letters = Console.ReadLine();
        var stdtoutWriter = Console.Out;
        Console.SetOut(Console.Error);
        string[] remaining = FilterWords(words, letters);
        Console.SetOut(stdtoutWriter);
        for (int i = 0; i < remaining.GetLength(0); i++)
        {
            Console.WriteLine(remaining[i]);
        }
    }
    /* Ignore and do not change the code above */
}