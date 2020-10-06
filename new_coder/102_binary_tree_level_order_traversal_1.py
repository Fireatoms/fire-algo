# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        ans, queue = [[root.val]], deque([root])
        while queue:
            level_length = len(queue)
            level = []
            for i in range(level_length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    level.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    level.append(node.right.val)

            if level:
                ans.append(level)

        return ans