# link: https://leetcode.com/problems/balanced-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.dfs(root)[1]

    def dfs(self, root):
        if not root:
            return 0, True

        l, res_l = self.dfs(root.left)
        r, res_r = self.dfs(root.right)

        if res_l and res_r and abs(l - r) <= 1:
            res = True
        else:
            res = False

        return max(l, r)+1, res


class SolutionIter:
    # preorder and layerorder both are ok.
    # the key is to handle child node before node
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        preorder_list = []
        stack = [root]
        while stack:
            node = stack.pop()
            preorder_list.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        node_depth = {None: 0}
        for node in reversed(preorder_list):
            left, right = node_depth[node.left], node_depth[node.right]
            if abs(left - right) > 1:
                return False
            node_depth[node] = max(left, right) + 1

        return True
