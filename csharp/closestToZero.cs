using System;

class A 
{
    /// This method finds the number closest to​​​​​​‌​​‌‌‌‌‌‌‌‌​‌​‌​‌​‌​​‌‌​‌ zero.
    public static int ClosestToZero(int[] ints) 
    {
        if (ints == null || ints.Length == 0) return 0;

        var closest = ints[0];

        for (var i = 0; i < ints.Length; i++) {
            var current = ints[i];

            if (Math.Abs(current) < Math.Abs(closest) || 
                (Math.Abs(current) == Math.Abs(closest) && current > 0 && closest < 0)) {
                    closest = current;
                }
        }

        return closest;
    }
}