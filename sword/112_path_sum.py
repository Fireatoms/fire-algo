# link: https://leetcode-cn.com/problems/path-sum/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = False

    def dfs(self, root, path_sum, target):
        if self.ans or not root:
            return
        path_sum += root.val
        if not root.left and not root.right:
            if path_sum == target:
                self.ans = True
        self.dfs(root.left, path_sum, target)
        self.dfs(root.right, path_sum, target)

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        self.dfs(root, 0, targetSum)
        return self.ans