# link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high-low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            elif nums[mid] == nums[high]:
                high -= 1
            else:
                high = mid
        return nums[low]

    def findMax(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high-low) // 2
            if nums[mid] < nums[high]:
                low = mid + 1
            elif nums[mid] == nums[high]:
                high -= 1
            else:
                high = mid
        return nums[low]


if __name__ == "__main__":
    arr = [2, 2, 6, 5, 4, 3, 3]
    sl = Solution()
    print(sl.findMax(arr))