# link: https://leetcode.com/problems/first-missing-positive/
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1

        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                nums = nums[i:]
                break

        # deduplication
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        if nums[0] <= 0:
            return 1

        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1

        return nums[-1] + 1

    # O(n) time
    def firstMissingPositive1(self, nums):
        # let i+1 be at position i
        for i in range(len(nums)):
            while 0 < nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
                tmp = nums[i] - 1
                nums[i], nums[tmp] = nums[tmp], nums[i]

        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1

        return len(nums) + 1

if __name__ == "__main__":
    nums = [1, 2, 0]
    sl = Solution()
    print(sl.firstMissingPositive(nums))