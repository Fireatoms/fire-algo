# link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        in_dict = {v: k for k, v in enumerate(inorder)}
        start = 0
        end = len(inorder) - 1
        return self.build_tree_r(in_dict, postorder, start, end)

    def build_tree_r(self, in_dict, postorder, start, end):
        if start > end:
            return None

        root_val = postorder.pop()
        inx = in_dict[root_val]
        root = TreeNode(root_val)
        root.right = self.build_tree_r(in_dict, postorder, inx + 1, end)
        root.left = self.build_tree_r(in_dict, postorder, start, inx - 1)

        return root