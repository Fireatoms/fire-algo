# link: https://leetcode.com/problems/binary-tree-level-order-traversal/
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        assist_queue = deque()
        # judge whether root is empty
        if root:
            assist_queue.append((root, 0))
        while assist_queue:
            node_layer = assist_queue.popleft()
            res.append((node_layer[0].val, node_layer[1]))
            if node_layer[0].left:
                assist_queue.append((node_layer[0].left, node_layer[1]+1))
            if node_layer[0].right:
                assist_queue.append((node_layer[0].right, node_layer[1]+1))

        res_list = {}
        multi_list = []
        for r in res:
            if r[1] not in res_list:
                res_list[r[1]] = []
            # res_list[r[1]] = res_list[r[1]].append(r[0])
            # too much times!!!
            res_list[r[1]].append(r[0])

        for i in range(len(res_list)):
            multi_list.append(res_list[i])

        return multi_list


class SolutionSimple:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root is None:
            return res
        assist_queue = deque([root])
        res.append([root.val])

        while assist_queue:
            l = len(assist_queue)
            level = []
            for i in range(l):
                head = assist_queue.popleft()
                if head.left:
                    assist_queue.append(head.left)
                    level.append(head.left.val)
                if head.right:
                    assist_queue.append(head.right)
                    level.append(head.right.val)
            if level:
                res.append(level)

        return res