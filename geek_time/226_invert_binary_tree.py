# link: https://leetcode-cn.com/problems/invert-binary-tree/
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTreeIterDfs(self, root: TreeNode) -> TreeNode:
        root_record = root
        stack = []
        if root: stack.append(root)

        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)

        return root_record

    def invertTreeIter(self, root: TreeNode) -> TreeNode:
        root_record = root
        queue = deque()
        if root: queue.append(root)

        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

        return root_record

    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root