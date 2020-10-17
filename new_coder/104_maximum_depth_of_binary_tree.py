# link: https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(root, 1)]
        ans = 1

        while stack:
            node, depth = stack.pop()
            ans = max(ans, depth)
            if node.left: stack.append((node.left, depth + 1))
            if node.right: stack.append((node.right, depth + 1))

        return ans

    def maxDepthRecursive(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_height = self.maxDepthRecursive(root.left)
        right_height = self.maxDepthRecursive(root.right)
        return max(left_height, right_height) + 1