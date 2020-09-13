# link: https://leetcode.com/problems/search-insert-position/


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high-low) // 2
            if nums[mid] >= target:
                if mid <= 0 or nums[mid-1] < target:
                    return mid
                else:
                    high = mid - 1
            else:
                low = mid + 1

        return len(nums)