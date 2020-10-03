# link: https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_idx = self.find_first_target(nums, target)
        if first_idx == -1:
            return [-1, -1]
        last_idx = self.find_last_target(nums, target)
        return [first_idx, last_idx]

    def find_first_target(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                if mid - 1 < 0 or nums[mid - 1] != target:
                    return mid
                else:
                    high = mid - 1
        return -1

    def find_last_target(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                if mid + 1 >= len(nums) or nums[mid + 1] != target:
                    return mid
                else:
                    low = mid + 1

        return -1