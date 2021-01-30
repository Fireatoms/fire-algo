# link: https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = 0

    def maxDepthDfs(self, root: TreeNode) -> int:
        if not root:
            return self.ans
        assist_stack = [(root, 1)]
        while assist_stack:
            root, depth = assist_stack.pop()
            if depth > self.ans: self.ans = depth
            if root.left: assist_stack.append((root.left, depth + 1))
            if root.right: assist_stack.append((root.right, depth + 1))
        return self.ans

    def maxDepthBfs(self, root: TreeNode) -> int:
        if not root:
            return self.ans
        assist_queue = deque([(root, 1)])
        while assist_queue:
            root, depth = assist_queue.popleft()
            if depth > self.ans: self.ans = depth
            if root.left: assist_queue.append((root.left, depth + 1))
            if root.right: assist_queue.append((root.right, depth + 1))
        return self.ans

    def dfs(self, root, depth):
        if depth > self.ans:
            self.ans = depth
        if root.left: self.dfs(root.left, depth + 1)
        if root.right: self.dfs(root.right, depth + 1)

    def maxDepth(self, root: TreeNode) -> int:
        if root:
            self.dfs(root, 1)
        return self.ans


if __name__ == "__main__":
    sl = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(sl.maxDepthDfs(root))