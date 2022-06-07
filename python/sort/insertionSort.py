# Function to do insertion sort
def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


# TODO: Approach 1: Brute Force - using the original way      [O(N^2) & O(1)]
# TODO: Approach 2: Binary Indexed Tree - https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/

def insertionSort1(arr):
    """
    type: List[int]
    rtype: int
    """
    totalSum = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]:
            totalSum += 1
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return totalSum


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]            # 7
    # arr = [2, 1, 3, 1, 2]             # 4
    # arr = [12, 15, 1, 5, 6, 14, 11]   # 10
    # arr = [3, 5, 7, 11, 9]            # 1

    # insertionSort(arr)
    # for i in range(len(arr)):
    #     print("% d" % arr[i], end=" ")

    print(insertionSort1(arr))
