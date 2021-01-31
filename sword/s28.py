# link: https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        assist_stack = [(root.left, root.right)]
        while assist_stack:
            left, right = assist_stack.pop()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            assist_stack.append((left.left, right.right))
            assist_stack.append((left.right, right.left))
        return True

    def isSymmetricRecur(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.is_symmetric_r(root.left, root.right)

    def is_symmetric_r(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False

        return self.is_symmetric_r(left.left, right.right) and self.is_symmetric_r(left.right, right.left)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    sl = Solution()
    print(sl.isSymmetric(root))
