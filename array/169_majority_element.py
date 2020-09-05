# link: https://leetcode.com/problems/majority-element/


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_dict = {}
        for num in nums:
            majority_dict[num] = majority_dict.get(num, 0) + 1
            if majority_dict[num] > len(nums) // 2:
                return num