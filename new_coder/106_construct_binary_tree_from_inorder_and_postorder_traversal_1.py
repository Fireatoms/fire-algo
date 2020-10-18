# link: https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        index_of_inorder = {v: i for i, v in enumerate(inorder)}
        return self.construct_tree_recur(postorder, index_of_inorder, 0, len(inorder) - 1)

    def construct_tree_recur(self, postorder, index_of_inorder, start, end):
        if start > end:
            return None

        root_val = postorder.pop()
        root = TreeNode(root_val)
        idx = index_of_inorder[root_val]
        root.right = self.construct_tree_recur(postorder, index_of_inorder, idx + 1, end)
        root.left = self.construct_tree_recur(postorder, index_of_inorder, start, idx - 1)
        return root