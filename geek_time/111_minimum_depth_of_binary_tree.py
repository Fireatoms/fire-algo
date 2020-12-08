# link: https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])
        while queue:
            root, depth = queue.popleft()
            if not root.left and not root.right:
                return depth
            if root.left: queue.append((root.left, depth+1))
            if root.right: queue.append((root.right, depth+1))