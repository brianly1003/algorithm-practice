
""" 
Input: [1, null, 2, 3]

            1
              \
               2
              /
            3

Output: [1, 3, 2]
 """


from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        return []

    def levelOrderTraversal1(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        stack, output = [], []
        current = root

        return output


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    s = Solution()
    print(s.inorderTraversal(root))
    # print(s.inorderTraversal1(root))
