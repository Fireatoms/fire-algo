# link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        low, high = 0, len(nums) - 1
        if nums[high] > nums[low]:
            return nums[low]

        while low <= high:
            mid = low + (high-low) // 2
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]

            if nums[0] < nums[mid]:
                low = mid + 1
            else:
                high = mid - 1