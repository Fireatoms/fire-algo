# link: https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums)
        low, high = 0, l - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            elif nums[mid] < nums[high]:
                high = mid
            else:
                high -= 1
        return nums[high]


if __name__ == "__main__":
    # nums = [2, 2, 2, 0, 1]
    nums = [1, 3, 3]
    sl = Solution()
    print(sl.findMin(nums))