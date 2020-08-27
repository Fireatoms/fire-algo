# link: https://leetcode.com/problems/minimum-depth-of-binary-tree/
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        level = []
        self.dfs(root, 0, level)
        return min(level)

    def dfs(self, root, ln, level):
        if not root.left and not root.right:
            level.append(ln+1)
        if root.left:
            self.dfs(root.left, ln+1, level)
        if root.right:
            self.dfs(root.right, ln+1, level)


class Solution1:
    # It is wrong way to get min level, but true to get max level.
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


class Solution2:
    # right recursive way
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left is None or root.right is None:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


class Solution3:
    # bfs
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        que = deque([(root, 0)])
        while que:
            node, level = que.popleft()
            if not node.left and not node.right:
                return level + 1
            if node.left:
                que.append((node.left, level+1))
            if node.right:
                que.append((node.right, level+1))