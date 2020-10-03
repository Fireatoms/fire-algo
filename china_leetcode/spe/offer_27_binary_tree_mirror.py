# link: https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)

        return root

    def mirrorTreeRecur(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        left = self.mirrorTree(root.left)
        right = self.mirrorTree(root.right)
        root.left = right
        root.right = left

        return root