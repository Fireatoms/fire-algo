# link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.middle_r(nums, 0, len(nums)-1)

    def middle_r(self, nums, low, high):
        if low > high:
            return None

        mid = (low + high) // 2
        node = TreeNode(nums[mid])
        node.left = self.middle_r(nums, low, mid - 1)
        node.right = self.middle_r(nums, mid + 1, high)
        return node