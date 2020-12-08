# link: https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_depth = 1

    def maxDepthIterBfs(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_depth = 1
        queue = deque([(root, 1)])
        while queue:
            root, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            if root.left: queue.append((root.left, depth+1))
            if root.right: queue.append((root.right, depth+1))
        return max_depth

    def maxDepthIterDfs(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        max_depth = 1
        while stack:
            root, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if root.right: stack.append((root.right, depth+1))
            if root.left: stack.append((root.left, depth+1))
        return max_depth

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1

    def maxDepthUpToDown(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.dfs(root, 1)
        return self.max_depth

    def dfs(self, root, depth):
        if not root.left and not root.right:
            self.max_depth = max(self.max_depth, depth)
            return
        if root.left: self.dfs(root.left, depth+1)
        if root.right: self.dfs(root.right, depth+1)


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sl = Solution()
    print(sl.maxDepthIterBfs(root))