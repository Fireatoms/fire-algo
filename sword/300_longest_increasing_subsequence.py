# link: https://leetcode-cn.com/problems/longest-increasing-subsequence/
from typing import List


class Solution:
    def lengthOfLIS_dp(self, nums: List[int]) -> int:
        nums_len = len(nums)
        dp = [1] * nums_len
        for i in range(nums_len):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def lengthOfLIS(self, nums: List[int]) -> int:
        ascend_list = []
        for num in nums:
            if not ascend_list or num > ascend_list[-1]:
                ascend_list.append(num)
            else:
                pos = self.get_first_le_pos(ascend_list, num)
                ascend_list[pos] = num
        return len(ascend_list)

    def get_first_le_pos(self, ascend_list, target):
        low, high = 0, len(ascend_list)
        while low <= high:
            mid = low + (high - low) // 2
            if ascend_list[mid] >= target:
                if mid < 1 or ascend_list[mid - 1] < target:
                    return mid
                else:
                    high = mid - 1
            else:
                low = mid + 1


if __name__ == "__main__":
    sl = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    res = sl.lengthOfLIS(nums)
    print(res)