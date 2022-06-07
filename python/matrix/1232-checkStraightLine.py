""" 1232. Check If It Is a Straight Line (Easy)
https://leetcode.com/problems/check-if-it-is-a-straight-line/
https://hoc247.net/hoi-dap/toan-10/viet-phuong-trinh-ham-so-y-ax-b-cua-dt-di-qua-a-1-1-va-voi-ox-faq41125.html

You are given an array coordinates, coordinates[i] = [x, y], where[x, y] represents the coordinate of a point.
Check if these points make a straight line in the XY plane.

*Input: coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
*Output: true

*Input: coordinates = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
*Output: false

!Constraints:
!2 <= coordinates.length <= 1000
!coordinates[i].length == 2
!-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
!coordinates contains no duplicate point.
 """

# TODO: Approach 1: Using linear equation y = ax + b    [0(N) & O(1)]
# TODO: Approach 2: Use ratio                           [O(N) & O(1)]


from typing import List


class Solution:
    def checkStraightLine1(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 1:
            return True

        x1, y1 = coordinates[0][0], coordinates[0][1]
        x2, y2 = coordinates[1][0], coordinates[1][1]

        if (x1 - x2) == 0:
            return False

        a = (y1 - y2) / (x1 - x2)
        b = y1 - a * x1

        for row in coordinates:
            if (row[1] != a * row[0] + b):
                return False

        return True

    def checkStraightLine2(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True

        x1, y1 = coordinates[0][0], coordinates[0][1]
        x2, y2 = coordinates[1][0], coordinates[1][1]

        if (x1 - x2) == 0:
            return False

        ratio = (y2 - y1) / (x2 - x1)

        for row in coordinates[2::]:
            ratio1 = (row[1] - y1) / (row[0] - x1)

            if abs(ratio1) != abs(ratio):
                return False

        return True

import math
if __name__ == "__main__":
    # coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]  # ? Output = true
    # coordinates = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]  # ? Output = false
    # coordinates = [[-3, -2], [-1, -2], [2, -2], [-2, -2], [0, -2]]
    coordinates = [[-7, -3], [-7, -1], [-2, -2],
                   [0, -8], [2, -2], [5, -6], [5, -5], [1, 7]]

    s = Solution()
    result1 = s.checkStraightLine1(coordinates)
    result2 = s.checkStraightLine2(coordinates)

    print("[Approach 1] Result is {}".format(result1))
    print("[Approach 2] Result is {}".format(result2))
