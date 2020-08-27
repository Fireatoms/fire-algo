# link: https://leetcode.com/problems/minimum-depth-of-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        level = []
        self.dfs(root, 0, level)
        return min(level)

    def dfs(self, root, ln, level):
        if not root.left and not root.right:
            level.append(ln+1)
        if root.left:
            self.dfs(root.left, ln+1, level)
        if root.right:
            self.dfs(root.right, ln+1, level)