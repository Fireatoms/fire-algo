# link: https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = True

    def dfs(self, root):
        if not root or not self.ans:
            return 0
        left_depth = self.dfs(root.left)
        right_depth = self.dfs(root.right)
        if abs(left_depth - right_depth) > 1:
            self.ans = False
        return max(left_depth, right_depth) + 1

    def isBalancedOrigin(self, root: TreeNode) -> bool:
        self.dfs(root)
        return self.ans

    def height(self, root):
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        return self.height(root) >= 0


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    root.right.left.right = TreeNode(8)
    sl = Solution()
    print(sl.isBalanced(root))
