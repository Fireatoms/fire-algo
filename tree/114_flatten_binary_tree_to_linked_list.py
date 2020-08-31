# link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# solution: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/37214/Python-recursive-solution-with-comments.
# it is too hard for me to understand: recursion


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        tail = root.left
        if tail:
            while tail.right:
                tail = tail.right
            tail.right = root.right
            root.right = root.left
            root.left = None