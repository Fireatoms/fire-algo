# link: https://leetcode-cn.com/problems/path-sum-ii/
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = []

    def dfs(self, root, path_sum, target, path):
        if not root:
            return
        path_sum += root.val
        path.append(root.val)
        if not root.left and not root.right:
            if path_sum == target:
                self.ans.append(path[:])

        self.dfs(root.left, path_sum, target, path)
        self.dfs(root.right, path_sum, target, path)
        # backtracking
        path.pop()

    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        self.dfs(root, 0, targetSum, [])
        return self.ans


if __name__ == "__main__":
    sl = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    print(sl.pathSum(root, 22))