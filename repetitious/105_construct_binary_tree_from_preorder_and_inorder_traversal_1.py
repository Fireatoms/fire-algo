# link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorder_dict = {v: i for i, v in enumerate(inorder)}
        preorder.reverse()
        return self.build_tree_r(preorder, inorder_dict, 0, len(preorder) - 1)

    def build_tree_r(self, preorder, inorder_dict, start, end):
        if start > end:
            return None

        root_val = preorder.pop()
        root = TreeNode(root_val)
        idx = inorder_dict[root_val]
        root.left = self.build_tree_r(preorder, inorder_dict, start, idx-1)
        root.right = self.build_tree_r(preorder, inorder_dict, idx+1, end)

        return root