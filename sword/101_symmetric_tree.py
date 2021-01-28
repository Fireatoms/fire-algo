# link: https://leetcode-cn.com/problems/symmetric-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetricRecur(self, root: TreeNode) -> bool:
        if root is None:
            return True

        def is_symmetric_r(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False

            return left.val == right.val and is_symmetric_r(left.left, right.right) and \
                   is_symmetric_r(left.right, right.left)
        return is_symmetric_r(root.left, root.right)

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        assist_stack = [(root.left, root.right)]
        while assist_stack:
            left, right = assist_stack.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            assist_stack.append((left.left, right.right))
            assist_stack.append((left.right, right.left))
        return True
    

if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(2)
    sl = Solution()
    print(sl.isSymmetric(root))