# link: https://leetcode-cn.com/problems/binary-tree-right-side-view/
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideViewBfs(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        right_most_value_at_depth = {}
        # max_depth = -1

        queue = deque()
        queue.append((root, 0))
        while queue:
            node, depth = queue.popleft()

            # max_depth = max(max_depth, depth)
            right_most_value_at_depth[depth] = node.val
            if node.left: queue.append((node.left, depth + 1))
            if node.right: queue.append((node.right, depth + 1))

        return [right_most_value_at_depth[depth] for depth in range(max(right_most_value_at_depth.keys()) + 1)]

    def rightSideViewDfs(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        right_most_value_at_depth = {}
        max_depth = -1

        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            right_most_value_at_depth.setdefault(depth, node.val)
            if node.left: stack.append((node.left, depth + 1))
            if node.right: stack.append((node.right, depth + 1))

        return [right_most_value_at_depth[depth] for depth in range(max_depth + 1)]