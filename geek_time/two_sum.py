# link: https://leetcode-cn.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for k, num in enumerate(nums):
            if target - num in cache:
                return [cache[target-num], k]
            cache[num] = k