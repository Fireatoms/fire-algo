# link: https://leetcode.com/problems/longest-increasing-subsequence/
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.lengthOfLIS_r(nums, float('-inf'), 0)

    def lengthOfLIS_r(self, nums, pre_val, cur_pos):
        if cur_pos == len(nums):
            return 0

        taken = 0
        if nums[cur_pos] > pre_val:
            taken = 1 + self.lengthOfLIS_r(nums, nums[cur_pos], cur_pos + 1)

        nottaken = self.lengthOfLIS_r(nums, pre_val, cur_pos + 1)
        return max(taken, nottaken)

    def lengthOfLIS_memo(self, nums: List[int]) -> int:
        memo = [[-1] * len(nums) for _ in range(len(nums))]
        return self.lengthOfLIS_memo_r(nums, -1, 0, memo)

    def lengthOfLIS_memo_r(self, nums, pre, cur, memo):
        if cur == len(nums):
            return 0

        if memo[pre][cur] >= 0:
            return memo[pre][cur]

        taken = 0
        if pre < 0 or nums[cur] > nums[pre]:
            taken = 1 + self.lengthOfLIS_memo_r(nums, cur, cur + 1, memo)

        notaken = self.lengthOfLIS_memo_r(nums, pre, cur + 1, memo)
        memo[pre][cur] = max(taken, notaken)
        return memo[pre][cur]

    def lengthOfLIS_dp(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    def lengthOfLIS_binary(self, nums: List[int]) -> int:
        assend_list = []

        for num in nums:
            if not assend_list or num > assend_list[-1]:
                assend_list.append(num)
            else:
                pos = 0
                low, high = 0, len(assend_list)
                while low <= high:
                    mid = low + (high - low) // 2
                    if assend_list[mid] >= num:
                        if mid == 0 or assend_list[mid - 1] < num:
                            pos = mid
                            break
                        else:
                            high = mid - 1
                    else:
                        low = mid + 1
                assend_list[pos] = num

        return len(assend_list)


if __name__ == "__main__":
    arr = [10,9,2,5,3,7,101,18]
    sl = Solution()
    print(sl.lengthOfLIS(arr))