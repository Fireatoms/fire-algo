# link: https://leetcode-cn.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for idx, num in enumerate(nums):
            if target - num in num_dict:
                return [num_dict[target - num], idx]
            else:
                num_dict[num] = idx