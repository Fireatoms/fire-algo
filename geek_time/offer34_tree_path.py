# link: https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def __init__(self):
        self.path = []
        self.current_sum = 0
        self.res = []

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.check_path(root, sum)
        return self.res

    def check_path(self, root, sum):
        if not root:
            return
        self.path.append(root.val)
        self.current_sum += root.val
        if not root.left and not root.right:
            if self.current_sum == sum:
                self.res.append(list(self.path))
        if root.left: self.check_path(root.left, sum)
        if root.right: self.check_path(root.right, sum)
        self.current_sum -= root.val
        self.path.pop()


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)

    sl = Solution()
    print(sl.pathSum(root, 22))