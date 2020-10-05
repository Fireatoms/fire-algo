# link: https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        index_of_inorder = {val: key for key, val in enumerate(inorder)}
        preorder.reverse()
        return self.build_tree_recur(preorder, index_of_inorder, 0, len(preorder) - 1)

    def build_tree_recur(self, preorder, index_of_inorder, start, end):
        if start > end:
            return None

        root_val = preorder.pop()
        root = TreeNode(root_val)
        idx = index_of_inorder[root_val]
        root.left = self.build_tree_recur(preorder, index_of_inorder, start, idx - 1)
        root.right = self.build_tree_recur(preorder, index_of_inorder, idx + 1, end)
        return root