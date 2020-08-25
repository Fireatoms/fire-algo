# link: https://leetcode.com/problems/binary-tree-postorder-traversal/
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.postorder_r(root, res)
        return res

    def postorder_r(self, root, res):
        if root is None:
            return
        self.postorder_r(root.left, res)
        self.postorder_r(root.right, res)
        res.append(root.val)

    def postorder_iteration(self, root):
        stack = []
        if root:
            stack.append(root)
        res = deque()
        while stack:
            node = stack.pop()
            res.appendleft(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return list(res)
