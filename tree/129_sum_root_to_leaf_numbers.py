# link: https://leetcode.com/problems/sum-root-to-leaf-numbers/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = [0]
        sum_record = 0
        self.dfs(root, sum_record, res)
        return res[0]

    def dfs(self, root, sum_record, res):
        if not root.left and not root.right:
            sum_record = 10 * sum_record + root.val
            res[0] = res[0] + sum_record
        if root.left:
            self.dfs(root.left, sum_record*10+root.val, res)
        if root.right:
            self.dfs(root.right, sum_record*10+root.val, res)