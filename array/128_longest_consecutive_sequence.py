# link: https://leetcode.com/problems/longest-consecutive-sequence/


class Solution:
    def longestConsecutiveBrute(self, nums: List[int]) -> int:
        longest_gap = 0
        for n in nums:
            current_num = n
            current_gap = 0
            while current_num + 1 in nums:
                current_num += 1
                current_gap += 1
            longest_gap = max(longest_gap, current_gap)

        return longest_gap

    def longestConsecutiveSort(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        longest_gap = 1
        current_gap = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1] + 1:
                    current_gap += 1
                else:
                    longest_gap = max(current_gap, longest_gap)
                    current_gap = 1
        return max(current_gap, longest_gap)

    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_gap = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num
                current_gap = 1
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_gap += 1

                longest_gap = max(longest_gap, current_gap)

        return longest_gap