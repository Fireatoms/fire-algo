# link: https://leetcode.com/problems/maximum-subarray/


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0], res = nums[0], nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            res = max(res, dp[i])

        return res

    def maxSubArrayLess(self, nums: List[int]) -> int:
        # link: https://leetcode.com/problems/maximum-subarray/discuss/20194/A-Python-solution
        cur_sum, max_sum = nums[0], nums[0]
        for num in nums[1:]:
            cur_sum = max(cur_sum+num, num)
            max_sum = max(max_sum, cur_sum)

        return max_sum