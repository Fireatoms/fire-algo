# link: https://leetcode.com/problems/symmetric-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isSym_r(root.left, root.right)

    def isSym_r(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False

        return p.val == q.val and self.isSym_r(p.left, q.right) and self.isSym_r(p.right, q.left)

    def is_symmetric_iteration(self, root):
        if root is None:
            return True

        stack = [(root.left, root.right)]
        while stack:
            p, q = stack.pop()
            if not p and not q:
                continue
            if not p or not q:
                return False
            if p.val != q.val:
                return False

            stack.append((p.left, q.right))
            stack.append((p.right, q.left))

        return True