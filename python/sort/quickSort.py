""" Quick Sort is a Devide and Conquer algorithm
https://www.geeksforgeeks.org/quick-sort/

1. Always pick first element as pivot.
2. Always pick last element as pivot. 
3. Pick a random element as pivot.
4. Pick median as pivot. """

from typing import List

class Solution:
    def quickSort(self, arr: List[int], low: int, high: int):
        if low < high:
            # pi is partitioning index, arr[pi] is now at right place
            pi = self.partition(arr, low, high)

            self.quickSort(arr, low, pi - 1)    # Before pi
            self.quickSort(arr, pi + 1, high)   # After pi

    def partition(self, arr: List[int], low: int, high: int):
        return 1
        