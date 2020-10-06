# link: https://leetcode-cn.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i, v in enumerate(nums):
            if target - v in cache:
                return [cache[target - v], i]
            cache[v] = i