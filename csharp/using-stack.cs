using System;
using System.Collections.Generic;

class Answer
{
    static public bool Check(string str)
    {
        var mapping = new Dictionary<char, char>() { { ']', '[' }, { ')', '(' }, { '}', '{' } };
        var stack = new Stack<char>();

        foreach (var c in str)
        {
            if (mapping.ContainsKey(c))
            {
                var top = stack.Count != 0 ? stack.Pop() : '#';
                if (mapping[c] != top)
                {
                    return false;
                }
            }
            else
            {
                stack.Push(c);
            }
        }

        return stack.Count == 0;
    }


    /// Checks that the given string is​​​​​​‌​​‌‌‌‌‌‌‌‌​‌​‌​‌‌​​​‌​​​ correct
    static public bool Check1(string str)
    {
        if (string.IsNullOrEmpty(str)) return true;

        Stack<char> stack = new Stack<char>();

        foreach (char c in str)
        {
            if (c == '(' || c == '[')
            {
                stack.Push(c);
            }
            else if (c == ')' && (stack.Count == 0 || stack.Peek() != '('))
            {
                return false;
            }
            else if (c == ']' && (stack.Count == 0 || stack.Peek() != '['))
            {
                return false;
            }
            else if (c == ')' || c == ']')
            {
                stack.Pop();
            }
        }

        return stack.Count == 0;
    }
}