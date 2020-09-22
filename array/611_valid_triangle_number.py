# link: https://leetcode.com/problems/valid-triangle-number/


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums) - 2):
            j = i + 1
            k = i + 2
            while j < len(nums) - 1 and nums[i] != 0:
                while k < len(nums) and nums[i] + nums[j] > nums[k]:
                    k += 1
                ans += k -j -1
                j += 1
        return ans