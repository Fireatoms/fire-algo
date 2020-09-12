# link: https://leetcode.com/problems/move-zeroes/


class Solution:
    def moveZeroesBrute(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        tmp = [0] * length
        i = 0
        for num in nums:
            if num != 0:
                tmp[i] = num
                i += 1

        nums[:] = tmp

    def moveZeroesSpaceSaving(self, nums: List[int]) -> None:
        i = 0
        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1

        nums[i:] = [0] * (len(nums)-i)

    def moveZeroes(self, nums: List[int]) -> None:
        first_zero, cur = 0, 0
        while cur < len(nums):
            if nums[cur] != 0:
                nums[first_zero], nums[cur] = nums[cur], nums[first_zero]
                first_zero += 1
            cur += 1
