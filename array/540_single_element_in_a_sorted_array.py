# link: https://leetcode.com/problems/single-element-in-a-sorted-array/


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            half_even_num = (high - mid) % 2 == 0
            if nums[mid] == nums[mid + 1]:
                if half_even_num:
                    low = mid + 2
                else:
                    high = mid - 1
            elif nums[mid] == nums[mid - 1]:
                if half_even_num:
                    high = mid - 2
                else:
                    low = mid + 1
            else:
                return nums[mid]

        return nums[low]

    def singleNonDuplicateImpove(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            else:
                high = mid

        return nums[low]