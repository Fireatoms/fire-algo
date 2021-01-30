# link: https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/
from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        assist_queue = deque([root])
        while assist_queue:
            l = len(assist_queue)
            level = []
            for i in range(l):
                root = assist_queue.popleft()
                level.append(root.val)
                if root.left: assist_queue.append(root.left)
                if root.right: assist_queue.append(root.right)
            ans.append(level)
        return ans


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    sl = Solution()
    print(sl.levelOrder(root))