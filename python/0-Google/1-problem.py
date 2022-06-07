# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Approach 1: Using one-pass HashTable          [O(n) & O(n)]

from typing import List


class Solution:
    def twoSum(self, nums: List[int], k: int) -> bool:
        Dict = {}

        for i in range(len(nums)):
            competent = k - nums[i]

            if competent in Dict:
                return True
            else:
                Dict[nums[i]] = i

        return False


if __name__ == "__main__":
    nums = [10, 15, 3, 7]
    k = 17

    s = Solution()
    print(s.twoSum(nums, k))
