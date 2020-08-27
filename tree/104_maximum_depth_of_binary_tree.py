# link: https://leetcode.com/problems/maximum-depth-of-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


class Solution1:
    # dfs
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(root, 0)]
        res = 0
        while stack:
            node, level = stack.pop()
            if not node.left and not node.right:
                res = max(level+1, res)
            if node.left:
                stack.append((node.left, level+1))
            if node.right:
                stack.append((node.right, level+1))

        return res