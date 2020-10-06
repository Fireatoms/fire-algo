# link: https://leetcode-cn.com/problems/maximum-subarray/


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [0] * length
        dp[0], ans = nums[0], nums[0]
        for i in range(1, length):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        return max(dp)

    def maxSubArrayImprove(self, nums: List[int]) -> int:
        length = len(nums)
        cur_sum, ans = nums[0], nums[0]

        for i in range(1, length):
            cur_sum = max(cur_sum + nums[i], nums[i])
            ans = max(cur_sum, ans)

        return ans