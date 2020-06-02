# link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 为了使用python的双向队列特性：两端的插入弹出时间复杂度都是o(1)
        pre_queue = deque(preorder)
        in_dict = {v: i for i, v in enumerate(inorder)}
        start = 0
        end = len(inorder) - 1
        # 返回整棵树的根结点
        return self.build_tree_r(pre_queue, in_dict, start, end)

    def build_tree_r(self, pre_queue, in_dict, start, end):
        if start > end:
            return None

        root_val = pre_queue.popleft()
        inx = in_dict[root_val]
        root = TreeNode(root_val)
        root.left = self.build_tree_r(pre_queue, in_dict, start, inx - 1)
        root.right = self.build_tree_r(pre_queue, in_dict, inx + 1, end)

        return root

