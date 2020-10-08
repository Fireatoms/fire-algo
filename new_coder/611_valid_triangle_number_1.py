# link: https://leetcode-cn.com/problems/valid-triangle-number/


class Solution:
    def triangleNumberBrute(self, nums: List[int]) -> int:
        length = len(nums)
        nums.sort()
        ans = 0
        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                for k in range(j + 1, length):
                    if nums[i] + nums[j] > nums[k]:
                        ans += 1

        return ans

    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        ans = 0
        for i in range(length - 2):
            j, k = i + 1, i + 2
            while j < length - 1 and nums[i] != 0:
                while k < length and nums[i] + nums[j] > nums[k]:
                    k += 1
                ans += k - j - 1
                j += 1

        return ans