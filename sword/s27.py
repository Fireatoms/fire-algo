# link: https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTreeIter(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        origin_root = root
        assist_stack = [root]
        while assist_stack:
            root = assist_stack.pop()
            root.left, root.right = root.right, root.left
            if root.left: assist_stack.append(root.left)
            if root.right: assist_stack.append(root.right)
        return origin_root

    def mirrorTree(self, root: TreeNode) -> TreeNode:
        self.mirror_r(root)
        return root

    def mirror_r(self, root):
        if not root:
            return root
        left = self.mirror_r(root.left)
        right = self.mirror_r(root.right)
        root.right = left
        root.left = right
        return root