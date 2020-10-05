# link: https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        ans = []
        queue = deque([root])
        ans.append([root.val])

        while queue:
            level = []
            length = len(queue)
            for i in range(length):
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