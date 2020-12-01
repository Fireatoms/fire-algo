# link: https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        index_of_inorder = {v: i for i, v in enumerate(inorder)}
        preorder.reverse()
        return self.build_tree_r(preorder, index_of_inorder, 0, len(preorder)-1)

    def build_tree_r(self, preorder, index_of_inorder, start, end):
        if start > end:
            return
        val = preorder.pop()
        index = index_of_inorder[val]
        root = TreeNode(val)
        root.left = self.build_tree_r(preorder, index_of_inorder, start, index-1)
        root.right = self.build_tree_r(preorder, index_of_inorder, index+1, end)
        return root