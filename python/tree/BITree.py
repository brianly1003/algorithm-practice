
# TODO: Approach 1: Binary Indexed Tree (BIT)           [O(logN)]
# TODO: N must be equal or greater than 12 if consider using Binary Indexed Tree
# https://www.geeksforgeeks.org/count-inversions-array-set-3-using-bit/


class Solution:
    def low_bit(self, t):
        return t & (-t)

    def getSum(self, BITree, index):
        _sum = 0
        index += 1

        while index > 0:
            _sum += BITree[index]
            index -= self.low_bit(index)

        return _sum

    def add(self, BITree, n, index, val):
        index += 1

        while index <= n:
            BITree[index] += val
            index += self.low_bit(index)

    def construct(self, arr, n):
        BITree = [0]*(n+1)

        for i in range(n):
            self.add(BITree, n, i, arr[i])

        return BITree

    def getInvCount(self, arr):
        invcount = 0  # Initialize result

        # Find maximum element in arrays
        maxElement = max(arr)

        # Create a BIT with size equal to maxElement+1
        # (Extra one is used so that elements can be directly be used as index)
        # for i in range(1, maxElement + 1):
        #     BITree[i] = 0
        BITree = [0] * (maxElement + 1)

        for i in range(len(arr) - 1, -1, -1):
            invcount += self.getSum(BITree, arr[i] - 1)
            self.add(BITree, maxElement, arr[i], 1)

        return invcount


if __name__ == "__main__":
    arr = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    # arr = [2, 1, 1, 3, 2]

    s = Solution()

    BITree = s.construct(arr, len(arr))
    print("Sum of elements in arr[0..5] is " + str(s.getSum(BITree, 5)))

    # arr[3] += 6
    # s.updatebit(BITree, len(arr), 3, 6)
    # print("Sum of elements in arr[0..5]" +
    #       " after update is " + str(s.getSum(BITree, 5)))

    print("Inversion Count : ", s.getInvCount(arr))
