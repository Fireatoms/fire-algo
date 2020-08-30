# link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        sorted_arr = []
        self._in_order(sorted_arr, root)
        return sorted_arr[k-1]

    def _in_order(self, sorted_arr, root):
        if not root:
            return

        self._in_order(sorted_arr, root.left)
        sorted_arr.append(root.val)
        self._in_order(sorted_arr, root.right)
