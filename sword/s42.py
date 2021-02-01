# link: https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        ans, cur = nums[0], nums[0]
        for i in range(1, nums_len):
            cur = max(cur + nums[i], nums[i])
            ans = max(cur, ans)
        return ans

    def maxSubArrayDp(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        dp = [0] * nums_len
        dp[0] = nums[0]
        for i in range(1, nums_len):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)


if __name__ == "__main__":
    sl = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(sl.maxSubArray(nums))