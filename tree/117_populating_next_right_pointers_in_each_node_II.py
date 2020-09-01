# link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/


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
        root_record = root
        pre_kid = Node(0)
        kid = pre_kid
        while root:
            while root:
                if root.left:
                    kid.next = root.left
                    kid = kid.next
                if root.right:
                    kid.next = root.right
                    kid = kid.next
                root = root.next

            root, kid = pre_kid.next, pre_kid
            kid.next = None

        return root_record