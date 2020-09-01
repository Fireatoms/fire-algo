# link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inorder_dict = {v: i for i, v in enumerate(inorder)}
        return self.build_tree_r(postorder, inorder_dict, 0, len(postorder)-1)

    def build_tree_r(self, postorder, inorder_dict, start, end):
        if start > end:
            return None

        root_val = postorder.pop()
        root = TreeNode(root_val)
        idx = inorder_dict[root_val]

        # the sequence matters
        # root.left = self.build_tree_r(postorder, inorder_dict, start, idx-1)
        root.right = self.build_tree_r(postorder, inorder_dict, idx+1, end)
        root.left = self.build_tree_r(postorder, inorder_dict, start, idx-1)
        return root