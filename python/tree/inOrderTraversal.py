
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        stack, output = [], []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            output.append(current.val)
            current = current.right

        return output

    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        output = []

        def helper(root: TreeNode):
            if root:
                if root.left:
                    helper(root.left)
                output.append(root.val)
                if root.right:
                    helper(root.right)

        helper(root)

        return output


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    s = Solution()
    # print(s.inorderTraversal(root))
    print(s.inorderTraversal1(root))
