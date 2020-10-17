# link: https://leetcode-cn.com/problems/maximum-subarray/


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length_nums = len(nums)
        dp = [float('-inf')] * length_nums
        dp[0] = nums[0]

        for i in range(1, length_nums):
            dp[i] = max(dp[i-1] + nums[i], nums[i])

        return max(dp)

    def maxSubArrayLowSpaceConsumption(self, nums: List[int]) -> int:
        length_nums = len(nums)
        ans, cur_sum = nums[0], nums[0]

        for i in range(1, length_nums):
            cur_sum = max(cur_sum + nums[i], nums[i])
            ans = max(cur_sum, ans)

        return ans