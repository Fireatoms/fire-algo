# link: https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        ans, queue = [[root.val]], deque([root])
        left_to_right = False
        while queue:
            level_list = []
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    level_list.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    level_list.append(node.right.val)

            if not left_to_right:
                level_list.reverse()

            left_to_right = not left_to_right

            if level_list:
                ans.append(level_list)

        return ans