from typing import List


class Solution:
    # TODO: One-pass HashTable O(N) & O(N)
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        dicts = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if (complement in dicts):
                return [dicts[complement], i]

            dicts[nums[i]] = i

        return []


if __name__ == "__main__":
    nums, target = [2, 7, 11, 15], 9  # Output: [0, 1]

    s = Solution()
    result = s.twoSum2(nums, target)

    print(f"Result = {result}")
