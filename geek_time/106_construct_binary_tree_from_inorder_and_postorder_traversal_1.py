# link: https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        index_of_inorder = {v: i for i, v in enumerate(inorder)}
        return self.build_tree_r(postorder, index_of_inorder, 0, len(inorder)-1)

    def build_tree_r(self, postorder, index_of_inorder, start, end):
        if start > end:
            return

        val = postorder.pop()
        index = index_of_inorder[val]
        root = TreeNode(val)
        root.right = self.build_tree_r(postorder, index_of_inorder, index+1, end)
        root.left = self.build_tree_r(postorder, index_of_inorder, start, index-1)
        return root