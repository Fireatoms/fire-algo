# link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
from collections import deque
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None

        res = [[root.val]]
        que = deque([root])
        left_to_right = False

        while que:
            level = deque()
            l = len(que)
            for i in range(l):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                    self.update_level(level, node.left.val, left_to_right)
                if node.right:
                    que.append(node.right)
                    self.update_level(level, node.right.val, left_to_right)

            if level:
                res.append(list(level))
            left_to_right = not left_to_right

        return res

    def update_level(self, level, val, left_to_right):
        if left_to_right:
            level.append(val)
        else:
            level.appendleft(val)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)

    sl = Solution()
    print(sl.zigzagLevelOrder(root))