using System;

class Solution
{
    /// <returns>the sum of integers whose index is between n1 and​​​​​​‌​​‌‌‌‌‌‌‌‌​‌​‌​‌​‌​‌‌​​‌ n2</returns>
	public static int Calc(int[] array, int n1, int n2) {
        var total = 0;

        for (var i = 0; i < array.Length; i++) {
            if (n1 <= i && i <= n2) {
                total += array[i];
            }
        }

        return total;
    }
}
