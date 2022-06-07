
from typing import List
import math

class Solution:
    def carParkingRoof(self, n: int, cars: List[int], k: int):
        result, j = math.inf, 0

        cars.sort()

        for i in range(n):
            j = i + k - 1;

            if j < n:
                result = min(result, cars[j] - cars[i] + 1)

        return 0 if result == math.inf else result


if __name__ == "__main__":
    # n, cars, k = 4, [6, 2, 12, 7], 3    #? Output = 6
    # n, cars, k = 4, [2, 10, 8, 17], 3   #? Output = 9
    n, cars, k = 4, [1, 2, 3, 10], 4      #? Output = 10

    s = Solution()
    result1 = s.carParkingRoof(n, cars, k)

    print("Result 1: {0}".format(result1))
    