# link: https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preorder.reverse()
        inorder_index = {v: i for i, v in enumerate(inorder)}
        return self.build_tree_recur(preorder, inorder_index, 0, len(inorder) - 1)

    def build_tree_recur(self, preorder, inorder_index, start, end):
        if start > end:
            return

        root_val = preorder.pop()
        root_index = inorder_index[root_val]
        root = TreeNode(root_val)
        root.left = self.build_tree_recur(preorder, inorder_index, start, root_index-1)
        root.right = self.build_tree_recur(preorder, inorder_index, root_index+1, end)

        return root