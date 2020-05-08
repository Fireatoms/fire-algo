# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        arr = []
        num = 0
        self.dfs(root, arr, num)
        return sum(arr)

    def dfs(self, node, arr, num):
        if node is None:
            return
        num = 10 * num + node.val
        if node.left is not None:
            self.dfs(node.left, arr, num)
        if node.right is not None:
            self.dfs(node.right, arr, num)
        if node.right is None and node.left is None:
            arr.append(num)