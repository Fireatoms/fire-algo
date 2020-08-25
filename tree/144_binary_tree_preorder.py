# link: https://leetcode.com/problems/binary-tree-preorder-traversal/
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.preorder_r(root, res)
        return res

    def preorder_r(self, root, res):
        if root:
            res.append(root.val)
            self.preorder_r(root.left, res)
            self.preorder_r(root.right, res)


class Solution1:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # iteration
        res = []
        stack = []
        if root: stack.append(root)
        while stack:
            top = stack.pop()
            res.append(top.val)
            if top.right: stack.append(top.right)
            if top.left: stack.append(top.left)

        return res


if __name__ == "__main__":
    root = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4

    sl1 = Solution1()
    res = sl1.preorderTraversal(root)
    print(res)