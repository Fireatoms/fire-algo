# link: https://leetcode.com/problems/find-the-duplicate-number/


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_set = set()
        for num in nums:
            if num not in nums_set:
                nums_set.add(num)
            else:
                return num

        return -1


class Solution1:
    def findDuplicate(self, nums):
        fast, slow = nums[0], nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break

        s1, s2 = nums[0], fast
        while s1 != s2:
            s1 = nums[s1]
            s2 = nums[s2]

        return s1


