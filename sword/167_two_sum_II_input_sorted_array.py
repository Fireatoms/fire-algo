# link: https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left+1, right+1]

    def twoSumMemo(self, numbers: List[int], target: int) -> List[int]:
        memo = {}
        for i in range(len(numbers)):
            matched_num = target - numbers[i]
            if matched_num in memo:
                return [memo[matched_num]+1, i+1]
            memo[numbers[i]] = i