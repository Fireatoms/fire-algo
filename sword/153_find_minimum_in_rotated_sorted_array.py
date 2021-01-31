# link: https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[high]


if __name__ == "__main__":
    sl = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    print(sl.findMin(nums))