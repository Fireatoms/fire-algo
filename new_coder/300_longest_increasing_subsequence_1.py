# link: https://leetcode-cn.com/problems/longest-increasing-subsequence/


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        length = len(nums)
        dp = [1] * length
        for i in range(length):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    def lengthOfLISGreedy(self, nums: List[int]) -> int:
        ascend_list = []
        for num in nums:
            if not ascend_list or num > ascend_list[-1]:
                ascend_list.append(num)
            else:
                pos = 0
                low, high = 0, len(ascend_list) - 1
                while low <= high:
                    mid = low + (high - low) // 2
                    if ascend_list[mid] >= num:
                        if mid < 1 or ascend_list[mid - 1] < num:
                            pos = mid
                            break
                        else:
                            high = mid - 1
                    else:
                        low = mid + 1
                
                ascend_list[pos] = num
        
        return len(ascend_list)