# link: https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestorOnce(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = root
        while ans:
            if ans.val > p.val and ans.val > q.val:
                ans = ans.left
            elif ans.val < p.val and ans.val < q.val:
                ans = ans.right
            else:
                return ans

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = self.get_path(root, p)
        q_path = self.get_path(root, q)
        p_length = len(p_path)
        q_length = len(q_path)

        i = 0
        ans = None
        while i < p_length and i < q_length and p_path[i] == q_path[i]:
            ans = p_path[i]
            i += 1
        return ans

    def get_path(self, root, target):
        path = []
        cur = root
        while cur.val != target.val:
            path.append(cur)
            if cur.val > target.val:
                cur = cur.left
            else:
                cur = cur.right
        path.append(cur)
        return path