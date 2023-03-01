using System;
using System.Collections.Generic;

class Answer
{
    /// Checks that the given string is​​​​​​‌​​‌‌‌‌‌‌‌‌​‌​‌​‌‌​​​‌​​​ correct
    static public bool Check(string str)
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