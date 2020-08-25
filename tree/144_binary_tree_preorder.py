# link: https://leetcode.com/problems/binary-tree-preorder-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.preorder_r(root, res)
        return res

    def preorder_r(self, root, res):
        if root:
            res.append(root.val)
            self.preorder_r(root.left, res)
            self.preorder_r(root.right, res)