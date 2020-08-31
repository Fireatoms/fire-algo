# link: https://leetcode.com/problems/count-complete-tree-nodes/
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = []
        que = deque([root])

        while que:
            node = que.popleft()
            res.append(node.val)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)

        return len(res)


class Solution1:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        ld = self.left_depth(root.left)
        rd = self.right_depth(root.right)
        if ld == rd:
            return 2 ** (ld+1) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def left_depth(self, root):
        depth = 0
        while root:
            depth += 1
            root = root.left
        return depth

    def right_depth(self, root):
        depth = 0
        while root:
            depth += 1
            root = root.right
        return depth