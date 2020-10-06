# link: https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dfs(root, p, q)
        return self.ans

    def dfs(self, root, p, q):
        if not root:
            return False

        lson = self.dfs(root.left, p, q)
        rson = self.dfs(root.right, p, q)
        if (lson and rson) or ((root == p or root == q) and (lson or rson)):
            self.ans = root
            # return  # not necessary
        return lson or rson or root == p or root == q

    def lowestCommonAncestorHash(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        queue = deque([root])
        parent_dict = {root: None}

        while p not in parent_dict or q not in parent_dict:
            node = queue.popleft()
            if node.left:
                parent_dict[node.left] = node
                queue.append(node.left)
            if node.right:
                parent_dict[node.right] = node
                queue.append(node.right)

        ancestor = set()
        while p:
            # p is itself parent
            ancestor.add(p)
            p = parent_dict[p]

        while q not in ancestor:
            q = parent_dict[q]

        return q

