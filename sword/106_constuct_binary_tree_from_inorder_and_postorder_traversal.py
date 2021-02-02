# link: https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inorder_index = {v: k for k, v in enumerate(inorder)}
        return self.build_tree_r(postorder, inorder_index, 0, len(postorder) - 1)

    def build_tree_r(self, postorder, inorder_index, start, end):
        if start > end:
            return
        node_val = postorder.pop()
        node = TreeNode(node_val)
        idx = inorder_index[node_val]
        node.right = self.build_tree_r(postorder, inorder_index, idx + 1, end)
        node.left = self.build_tree_r(postorder, inorder_index, start, idx - 1)
        return node