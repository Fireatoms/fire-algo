# link: https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        min_depth = float('inf')
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)

        return min_depth + 1

    def minDepthIter(self, root: TreeNode) -> int:
        if not root:
            return 0

        ans = float('inf')
        stack = [(root, 0)]

        while stack:
            node, depth = stack.pop()
            if not node.left and not node.right:
                ans = min(ans, depth + 1)
            if node.left: stack.append((node.left, depth + 1))
            if node.right: stack.append((node.right, depth + 1))

        return ans

    def minDepthIterQueue(self, root: TreeNode) -> int:
        if not root:
            return 0

        ans = float('inf')
        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right:
                ans = min(ans,  depth + 1)
            if node.left: queue.append((node.left, depth + 1))
            if node.right: queue.append((node.right, depth + 1))

        return ans