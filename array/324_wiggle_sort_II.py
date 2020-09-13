# link: https://leetcode.com/problems/wiggle-sort-ii/
from typing import List


class Solution:
    # wrong
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = sorted(nums, reverse=True)
        nums[1::2], nums[::2] = arr[:len(nums)//2], arr[len(nums)//2:]


if __name__ == "__main__":
    arr = [1,5,1,1,6,4]
    sl = Solution()
    sl.wiggleSort(arr)
    print(arr)