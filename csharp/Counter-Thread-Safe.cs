
class Counter
{
    private static int count = 0;
    private static readonly object lockObj = new object(); // create an object to use as a lock

    /// Increments count in a thread-safe​​​​​​‌​​‌‌‌‌‌‌‌‌​‌​‌​​‌​‌‌​‌‌‌ manner.
    public static int Increment()
    {
        lock (lockObj) // acquire the lock before modifying the count variable
        {
            count = count + 1;
            return count;
        }
    }
}

