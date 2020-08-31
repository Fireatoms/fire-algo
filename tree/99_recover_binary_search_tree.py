# link: https://leetcode.com/problems/recover-binary-search-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # sentry to simplify the processing of first node
        self.pre_node = TreeNode(float('-inf'))
        self.first, self.second = None, None
        self.in_order(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def in_order(self, root):
        if not root:
            return

        self.in_order(root.left)
        if not self.first and self.pre_node.val > root.val:
            self.first = self.pre_node
        if self.first and self.pre_node.val > root.val:
            self.second = root
        # pre_node after processing is completed
        self.pre_node = root
        self.in_order(root.right)

if __name__ == "__main__":
    sl = Solution()
