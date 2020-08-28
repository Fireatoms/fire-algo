# link: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None

        res = deque([[root.val]])
        # problem 102: res = [] stack
        que = deque([root])

        while que:
            level = []
            l = len(que)
            # the length of que will change, so it is necessary to record the init length of que at beginning
            # for i in range(len(que)):
            for i in range(l):
                node = que.popleft()
                if node.left:
                    level.append(node.left.val)
                    que.append(node.left)
                if node.right:
                    level.append(node.right.val)
                    que.append(node.right)

            if level:
                res.appendleft(level)

        return list(res)
