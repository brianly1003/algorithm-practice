using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using System.Linq;
using System.Text;
using System.Threading;

class Solution
{
    /// Counts the number of pairs for n​​​​​​‌​​‌‌‌‌‌‌‌‌​‌​‌​‌‌​​​​​‌‌ players.
    public static int Count(int n)
    {
        return n * (n - 1) / 2;
    }
}

/* 
You have to organize a chess tournament in which players will compete head-to-head.

Here is how we proceed to form the duels: select a first player randomly, then, select his opponent at random among the remaining participants. The pair of competitors obtained forms one of the duels of the tournament. We proceed in the same manner to form all the other pairs.

In this exercise, we would like to know how many pairs it is possible to form knowing that the order of opponents in a pair does not matter.

For example, with 4 players named A, B, C and D, it is possible to get 6 different pairs : AB, AC, AD, BC, BD, CD.

Implement Count to return the number of possible pairs. Parameter n corresponds to the number of players.

Try to optimize your solution so that, ideally, the duration of treatment is the same for any n.

Input: 2 <= n <= 10000 

*/