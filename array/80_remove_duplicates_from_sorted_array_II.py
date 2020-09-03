# link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for n in nums:
            if i < 2 or nums[i-2] < n:
                nums[i] = n
                i += 1
        return i