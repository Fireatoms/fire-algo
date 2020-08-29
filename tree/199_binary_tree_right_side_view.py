# link: https://leetcode.com/problems/binary-tree-right-side-view/
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return None

        res = [root.val]
        que = deque([root])

        while que:
            l = len(que)
            level = []
            for i in range(l):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                    level.append(node.left.val)
                if node.right:
                    que.append(node.right)
                    level.append(node.right.val)

            if level:
                res.append(level[-1])

        return res