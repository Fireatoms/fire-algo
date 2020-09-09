# link: https://leetcode.com/problems/sort-colors/
from collections import Counter
from typing import List


class Solution:
    def sortColorsCount(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = Counter(nums)
        nums[:] = [0] * cnt[0] + [1] * cnt[1] + [2] * cnt[2]

    def sortColors(self, nums: List[int]) -> None:
        p0, cur, p2 = 0, 0, len(nums) - 1
        while cur <= p2:
            if nums[cur] == 0:
                nums[cur], nums[p0] = nums[p0], nums[cur]
                cur += 1
                p0 += 1
            elif nums[cur] == 2:
                nums[p2], nums[cur] = nums[cur], nums[p2]
                p2 -= 1
            else:
                cur += 1


if __name__ == "__main__":
    arr = [2,0,2,1,1,0]
    sl = Solution()
    sl.sortColorsCount(arr)