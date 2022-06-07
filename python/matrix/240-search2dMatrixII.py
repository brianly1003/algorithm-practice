
# 240. Search a 2D Matrix II (Easy)
# https://leetcode.com/problems/search-a-2d-matrix-ii/
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

# Consider the following matrix:
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.
# Given target = 20, return false.

# TODO: Approach 1: Brute Force             [O(m*m) & O(1)]
# TODO: Approach 2: Binary Search           [O(log(N!)) & O(1)]    
# TODO: Approach 3: Divide and Conquer      [O(NlogN) & O(1)]
# TODO: Approach 4: Search Space Reduction  [O(n+m) & O(1)]

class Solution:
    def searchMatrix1(self, maxtrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        for row in matrix:
            if target in row:
                return True

        return False


if __name__ == "__main__":
    matrix = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

    # target = 5
    target = 20

    s = Solution()
    print(s.searchMatrix1(matrix, target))
