# link: https://leetcode-cn.com/problemset/lcof/?difficulty=%E7%AE%80%E5%8D%95
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        i = 0
        for j in range(len(nums)):
            if nums[j] % 2 == 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums


if __name__ == "__main__":
    sl = Solution()
    nums = [1,2,3,4]
    print(sl.exchange(nums))