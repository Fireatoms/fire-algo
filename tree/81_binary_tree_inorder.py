# link: https://leetcode.com/problems/binary-tree-inorder-traversal/


# link: https://leetcode.com/problems/binary-tree-inorder-traversal/
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.inorder_r(root, res)
        return res

    def inorder_r(self, root, res):
        if root is None:
            return
        self.inorder_r(root.left, res)
        res.append(root.val)
        self.inorder_r(root.right, res)

    def inorder_iteration(self, root):
        res = []
        stack = []
        while root or stack:
            # put all left nodes into stack
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            res.append(node.val)
            # begin with right node
            root = node.right
        return res