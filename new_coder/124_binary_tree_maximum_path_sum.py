# link: https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_sum = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        self.max_gain(root)
        return self.max_sum

    def max_gain(self, root):
        if not root:
            return 0

        left_gain = max(self.max_gain(root.left), 0)
        right_gain = max(self.max_gain(root.right), 0)
        self.max_sum = max(self.max_sum, left_gain + right_gain + root.val)

        return root.val + max(left_gain, right_gain)


if __name__ == "__main__":
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(3)
    sl = Solution()
    print(sl.maxPathSum(root))