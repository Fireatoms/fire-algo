# link: https://leetcode-cn.com/problems/binary-tree-inorder-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            ans.append(node.val)
            root = node.right

        return ans