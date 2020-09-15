# link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
from typing import List

class Solution:
    # 1. find the first num equal to target
    # 2. find the last num equal to target
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.first_equal_to_target(nums, target)
        if left == -1:
            return [-1, -1]
        right = self.last_equal_to_target(nums, target)
        return [left, right]

    def first_equal_to_target(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high-low) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid-1] != target:
                    return mid
                else:
                    high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1

    def last_equal_to_target(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high-low) // 2
            if nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid+1] != target:
                    return mid
                else:
                    low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1


if __name__ == "__main__":
    arr = [5,7,7,8,8,10]
    sl = Solution()
    print(sl.first_equal_to_target(arr, 8))