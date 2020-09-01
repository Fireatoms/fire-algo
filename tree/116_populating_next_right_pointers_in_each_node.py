# link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        que = deque([root])
        while que:
            l = len(que)
            pre = None
            for i in range(l):
                node = que.popleft()
                if pre:
                    pre.next = node
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                pre = node
            # not necessary, because the node points to None by default
            # pre.next = None

        return root


class SolutionRecursive:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        # necessary when handle node in last layer
        if root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)

        return root


