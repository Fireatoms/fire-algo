# link: https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
import unittest
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_depth = 0

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return self.max_depth
        # self.bfs_recur([root], 1)
        # self.dfs_recur(root, 1)
        # self.bfs_iter(root)
        self.dfs_iter(root)
        return self.max_depth

    def bfs_recur(self, level_nodes, level):
        if not level_nodes:
            return

        self.max_depth = max(self.max_depth, level)
        next_level_nodes = []
        for node in level_nodes:
            if node.left: next_level_nodes.append(node.left)
            if node.right: next_level_nodes.append(node.right)

        if next_level_nodes:
            self.bfs_recur(next_level_nodes, level + 1)

    def dfs_recur(self, root, level):
        if not root:
            return

        self.max_depth = max(self.max_depth, level)
        if root.left: self.dfs_recur(root.left, level + 1)
        if root.right: self.dfs_recur(root.right, level + 1)

    def bfs_iter(self, root):
        queue = deque()
        queue.append((root, 1))
        while queue:
            node, level = queue.popleft()
            self.max_depth = max(self.max_depth, level)
            if node.left: queue.append((node.left, level + 1))
            if node.right: queue.append((node.right, level + 1))

    def dfs_iter(self, root):
        stack = [(root, 1)]
        while stack:
            node, level = stack.pop()
            self.max_depth = max(self.max_depth, level)
            if node.left: stack.append((node.left, level + 1))
            if node.right: stack.append((node.right, level + 1))


class TestSolution(unittest.TestCase):
    def test_max_depth(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.left.right.left = TreeNode(6)
        root.left.right.right = TreeNode(7)
        sl = Solution()
        self.assertEqual(sl.maxDepth(root), 4)


if __name__ == "__main__":
    unittest.main()