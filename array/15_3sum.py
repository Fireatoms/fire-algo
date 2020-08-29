# link: https://leetcode.com/problems/3sum/
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        i = 0
        res = []
        while i < l - 2:
            #  1 2 2 3: i = 0 i = 1 i = 4, skip i = 2
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            j = i + 1
            k = l - 1

            while j < k:
                if nums[j] + nums[k] < -nums[i]:
                    j += 1
                elif nums[j] + nums[k] > -nums[i]:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j+1] == nums[j]:
                        j += 1
                    while j < k and nums[k-1] == nums[k]:
                        k -= 1
                    j += 1
                    k -= 1
            i += 1

        return res


if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    sl = Solution()
    print(sl.threeSum(arr))