# link: https://leetcode.com/problems/binary-tree-maximum-path-sum/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.res = root.val
        self.max_sum_child(root)
        return self.res

    def max_sum_child(self, root):
        if not root:
            return 0

        l = max(0, self.max_sum_child(root.left))
        r = max(0, self.max_sum_child(root.right))
        self.res = max(self.res, l+r+root.val)
        return root.val + max(l, r)