# link: https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
from collections import deque
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = []

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        self.dfs(root, 0)
        return self.res

    def dfs(self, node, level):
        if not node:
            return
        if level > len(self.res) - 1:
            self.res.append([])
        self.res[level].append(node.val)
        self.dfs(node.left, level+1)
        self.dfs(node.right, level+1)

    def levelOrderBfs(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        res = []
        while queue:
            level = []
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if level:
                res.append(level)
        return res


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(6)
    root.left.right.right = TreeNode(7)

    sl = Solution()
    print(sl.levelOrder(root))