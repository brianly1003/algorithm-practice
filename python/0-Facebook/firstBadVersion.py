""" 278. First Bad Version (Easy)
https://leetcode.com/problems/first-bad-version/

You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. 
You should minimize the number of calls to the API. """

# * Example:
# * Given n = 5, and version = 4 is the first bad version.

# *     call isBadVersion(3) -> false
# *     call isBadVersion(5) -> true
# *     call isBadVersion(4) -> true

# * Then 4 is the first bad version.

# TODO: Approach 2: Binary Search           [O(logN) & O(1)]


def isBadVersion(version: int) -> bool:
    falsy = [4, 5, 6, 7, 8, 9, 10]

    if version in falsy:
        return True

    return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left < right:
            mid = left + (right - left) // 2
            if (isBadVersion(mid)):
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    N = 10

    s = Solution()
    print(s.firstBadVersion(N))
