# link: https://leetcode.com/problems/balanced-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.dfs(root)[1]

    def dfs(self, root):
        if not root:
            return 0, True

        l, res_l = self.dfs(root.left)
        r, res_r = self.dfs(root.right)

        if res_l and res_r and abs(l - r) <= 1:
            res = True
        else:
            res = False

        return max(l, r)+1, res