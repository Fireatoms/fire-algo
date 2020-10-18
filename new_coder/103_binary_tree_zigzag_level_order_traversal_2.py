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
            level_length = len(queue)
            level_list = []

            for i in range(level_length):
                node = queue.popleft()
                if node.left:
                    level_list.append(node.left.val)
                    queue.append(node.left)
                if node.right:
                    level_list.append(node.right.val)
                    queue.append(node.right)

            if not left_to_right:
                level_list.reverse()

            left_to_right = not left_to_right
            if level_list: ans.append(level_list)

        return ans