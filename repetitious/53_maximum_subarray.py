# link: https://leetcode.com/problems/maximum-subarray/


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        # Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
        # so dp[0] = nums[0]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)

    def maxSubArrayImpove(self, nums: List[int]) -> int:
        cur_sum, max_sum = nums[0], nums[0]
        for num in nums[1:]:
            cur_sum = max(cur_sum + num, num)
            max_sum = max(cur_sum, max_sum)
        return max_sum