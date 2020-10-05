# link: https://leetcode-cn.com/problems/3sum/
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        ans = []

        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # two sum
            j, k = i + 1, length - 1
            while j < k:
                if nums[j] + nums[k] < -nums[i]:
                    j += 1
                elif nums[j] + nums[k] > -nums[i]:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k - 1] == nums[k]:
                        k -= 1
                    j += 1
                    k -= 1

        return ans


if __name__ == "__main__":
    nums = [1,-1,-1,0]
    sl = Solution()
    sl.threeSum(nums)