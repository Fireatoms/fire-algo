# link: https://leetcode.com/problems/invert-binary-tree/
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root

    def invertTreeDfs(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                tmp = node.left
                node.left = node.right
                node.right = tmp
                stack.append(node.left)
                stack.append(node.right)

        return root

    def invert_tree_bfs(self, root):
        if root is None:
            return None

        que = deque([root])
        while que:
            node = que.popleft()
            if node:
                node.left, node.right = node.right, node.left
                que.append(node.left)
                que.append(node.right)

        return root