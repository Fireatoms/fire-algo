# link: https://leetcode.com/problems/same-tree/
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTreeIteration(self, p: TreeNode, q: TreeNode) -> bool:
        assist_queue = deque([(p, q)])
        while assist_queue:
            p, q = assist_queue.popleft()
            if not self.check(p, q):
                return False
            if p:
                # p is not None, so q must not be None
                assist_queue.append((p.left, q.left))
                assist_queue.append((p.right, q.right))

        return True


    def check(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return True
