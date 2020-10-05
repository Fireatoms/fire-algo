# link: https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
         pre_index = self.find_first_equal_element(nums, target)
         if pre_index == -1:
             return [-1, -1]

         post_index = self.find_last_equal_element(nums, target)
         return [pre_index, post_index]

    def find_first_equal_element(self, nums, target):
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

    def find_last_equal_element(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                if mid + 1 > len(nums) - 1 or nums[mid + 1] != target:
                    return mid
                else:
                    low = mid + 1

        return -1