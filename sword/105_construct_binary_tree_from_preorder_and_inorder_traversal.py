# link: https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorder_index = {v: k for k, v in enumerate(inorder)}
        preorder.reverse()
        return self.build_tree_r(preorder, inorder_index, 0, len(preorder) - 1)

    def build_tree_r(self, preorder, inorder_index, start, end):
        if start > end:
            return
        node_val = preorder.pop()
        node = TreeNode(node_val)
        idx = inorder_index[node_val]
        node.left = self.build_tree_r(preorder, inorder_index, start, idx - 1)
        node.right = self.build_tree_r(preorder, inorder_index, idx + 1, end)
        return node
