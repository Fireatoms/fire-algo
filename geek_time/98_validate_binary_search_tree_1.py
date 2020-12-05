# link: https://leetcode-cn.com/problems/validate-binary-search-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.pre = float("-inf")

    def isValidBST_iter(self, root: TreeNode) -> bool:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= self.pre:
                return False
            self.pre = root.val
            root = root.right
        return True

    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True

        if not self.isValidBST(root.left):
            return False
        if root.val <= self.pre:
            return False
        self.pre = root.val
        return self.isValidBST(root.right)