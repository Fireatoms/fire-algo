# link: https://leetcode.com/problems/path-sum/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        res = []
        self.dfs(root, 0, res)
        if sum in res:
            return True
        return False

    def dfs(self, root, sum_res, res):
        if not root.left and not root.right:
            res.append(sum_res+root.val)
        if root.left:
            self.dfs(root.left, sum_res+root.val, res)
        if root.right:
            self.dfs(root.right, sum_res+root.val, res)

    def hasPathSumStack(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        stack = [(root, 0)]
        res = []
        while stack:
            node, sum_res = stack.pop()
            if not node.left and not node.right:
                res.append(sum_res+node.val)
            if node.left:
                stack.append((node.left, sum_res+node.val))
            if node.right:
                stack.append((node.right, sum_res+node.val))
        if sum in res:
            return True
        return False