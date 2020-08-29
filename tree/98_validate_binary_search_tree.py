# link: https://leetcode.com/problems/validate-binary-search-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # the value of root node is greater than its left subtree but less than right subtree
    def isValidBST(self, root: TreeNode) -> bool:
        return self.is_valid_r(root, None, None)

    def is_valid_r(self, root, min, max):
        if not root:
            return True

        if min and root.val <= min.val:
            return False
        if max and root.val >= max.val:
            return False

        return self.is_valid_r(root.left, min, root) and self.is_valid_r(root.right, root, max)


class Solution1:
    # the value of root node is greater than its left subtree but less than right subtree
    # dfs
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, min, max = stack.pop()
            if node.val <= min or node.val >= max:
                return False
            if node.left:
                stack.append((node.left, min, node.val))
            if node.right:
                stack.append((node.right, node.val, max))

        return True


class Solution2:
    # the value of root node is greater than its left subtree but less than right subtree
    # inorder
    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            node = stack.pop()
            if node.val <= inorder:
                return False
            inorder = node.val
            root = node.right

        return True
