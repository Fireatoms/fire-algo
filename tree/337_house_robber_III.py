# link: https://leetcode.com/problems/house-robber-iii/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.dfs(root))

    def dfs(self, node):
        if not node:
            return 0, 0

        l = self.dfs(node.left)
        r = self.dfs(node.right)
        return max(l) + max(r), node.val + l[0] + r[0]
