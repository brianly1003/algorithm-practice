// C# code​​​​​​‌​​‌‌‌‌‌‌‌‌​‌​‌​‌​‌‌‌​​​‌ below
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using System.Linq;
using System.Text;
using System.Threading;

class Solution
{
    public static bool isTwin(String a, String b)
    {
        // Convert both strings to lowercase and sort their characters
        char[] aChars = a.ToLower().ToCharArray();
        Array.Sort(aChars);
        char[] bChars = b.ToLower().ToCharArray();
        Array.Sort(bChars);

        // Compare the sorted character arrays for equality
        return new string(aChars) == new string(bChars);
    }
}