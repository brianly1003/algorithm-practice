

from typing import List
import math


class Solution:
    def closestToZero(self, ints: List[int]):
        if ints is None or len(ints) == 0:
            return 0

        closest = ints[0]

        for num in ints:
            if abs(num) < abs(closest):
                closest = num
            elif abs(num) == abs(closest):
                closest = max(closest, num)

        return closest


if __name__ == "__main__":
    # ints = [7, 5, 9, 1, 4]  # ? Output: 1
    # ints = [-7, -5, -9, -1, -4]  # ? Output: -1
    ints = [-7, -5, -9, 5, 6]  # ? Output: 5

    s = Solution()
    result = s.closestToZero(ints)

    print(f"Result is {result}")
