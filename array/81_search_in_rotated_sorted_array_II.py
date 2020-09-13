# link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high-low) // 2
            if nums[mid] == target:
                return True

            if nums[low] < nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[low] > nums[mid]:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                low += 1

        return False


if __name__ == "__main__":
    sl = Solution()
    arr = [1, 3, 1, 1, 1]
    sl.search(arr, 3)