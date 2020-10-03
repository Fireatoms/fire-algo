# link: https://leetcode-cn.com/problems/binary-tree-inorder-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans, stack = [], []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            ans.append(node.val)
            root = node.right
        return ans

    def inorderTraversalRecur(self, root: TreeNode) -> List[int]:
        ans = []
        self.inorder_r(root, ans)
        return ans

    def inorder_r(self, root, ans):
        if not root:
            return

        self.inorder_r(root.left, ans)
        ans.append(root.val)
        self.inorder_r(root.right, ans)