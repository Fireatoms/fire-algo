# link: https://leetcode.com/problems/binary-tree-paths/
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []
        res = []
        self.dfs(root, '', res)
        return res

    def dfs(self, root, path_str, res):
        if not root.left and not root.right:
            res.append(path_str + str(root.val))

        if root.left:
            self.dfs(root.left, path_str + str(root.val) + '->', res)
        if root.right:
            self.dfs(root.right, path_str + str(root.val) + '->', res)

    def binaryTreePathsStack(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        stack = [(root, '')]
        res = []
        while stack:
            node, path_str = stack.pop()
            if not node.left and not node.right:
                res.append(path_str+str(node.val))

            if node.left:
                stack.append((node.left, path_str+str(node.val)+'->'))
            if node.right:
                stack.append((node.right, path_str+str(node.val)+'->'))
        return res

    def binaryTreePathsQueue(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        que = deque([(root, '')])
        res = []
        while que:
            node, path_str = que.popleft()
            if not node.left and not node.right:
                res.append(path_str+str(node.val))
            if node.left:
                que.append((node.left, path_str+str(node.val)+'->'))
            if node.right:
                que.append((node.right, path_str+str(node.val)+'->'))

        return res