# link: https://leetcode.com/problems/minimum-size-subarray-sum/


class Solution:
    def minSubArrayLenBrute(self, s: int, nums: List[int]) -> int:
        res = float('inf')
        for i in range(len(nums)):
            con_sum = 0
            for j in range(i, len(nums)):
                con_sum += nums[j]
                if con_sum >= s:
                    res = min(res, j-i+1)
                    break
        return res if res != float('inf') else 0

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left, sum = 0, 0
        ans = float('inf')
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= s:
                ans = min(ans, i-left+1)
                sum -= nums[left]
                left += 1

        return ans if ans != float('inf') else 0



