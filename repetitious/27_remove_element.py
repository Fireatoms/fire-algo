# link: https://leetcode.com/problems/remove-element/
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums) - 1
        # index i must be checked also
        while i <= j:
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1
        return i


if __name__ == "__main__":
    nums = [4, 2, 3, 5]
    sl = Solution1()
    print(sl.removeElement(nums, 5))