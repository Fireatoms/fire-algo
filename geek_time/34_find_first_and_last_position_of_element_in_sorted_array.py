# link: https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_border = self.first_equal(nums, target)
        if left_border == -1:
            return [-1, -1]
        right_border = self.last_equal(nums, target)
        return [left_border, right_border]

    def first_equal(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                if mid <= 0 or nums[mid-1] != target:
                    return mid
                else:
                    high = mid - 1

        return -1

    def last_equal(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                if mid >= len(nums) - 1 or nums[mid+1] != target:
                    return mid
                else:
                    low = mid + 1

        return -1


if __name__ == "__main__":
    arr = [1, 2, 2, 3, 3, 3, 4, 5]
    sl = Solution()
    print(sl.searchRange(arr, 3))