# link: https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        if not nums:
            return -1
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                tmp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = tmp

    def findRepeatNumberHash(self, nums: List[int]) -> int:
        assist_set = set()
        for num in nums:
            if num in assist_set:
                return num
            assist_set.add(num)