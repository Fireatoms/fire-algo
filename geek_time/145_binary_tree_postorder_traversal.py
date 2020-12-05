# link: https://leetcode-cn.com/problems/binary-tree-postorder-traversal/
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return

        res = deque()
        stack = [root]
        while stack:
            node = stack.pop()
            res.appendleft(node.val)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)

        return list(res)