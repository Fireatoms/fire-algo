# link: https://leetcode-cn.com/problems/3sum/
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums_len = len(nums)
        res = []
        for i in range(nums_len):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            j, k = i + 1, nums_len - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
        return res


if __name__ == "__main__":
    sl = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(sl.threeSum(nums))