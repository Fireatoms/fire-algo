# link: https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inorder_index = {v: i for i, v in enumerate(inorder)}
        return self.build_tree_recur(postorder, inorder_index, 0, len(inorder)-1)

    def build_tree_recur(self, postorder, inorder_index, start, end):
        if start > end:
            return

        root_val = postorder.pop()
        root_index = inorder_index[root_val]
        root = TreeNode(root_val)
        root.right = self.build_tree_recur(postorder, inorder_index, root_index+1, end)
        root.left = self.build_tree_recur(postorder, inorder_index, start, root_index-1)

        return root