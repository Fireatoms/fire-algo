# link: https://leetcode.com/problems/permutations/
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        k = len(nums)
        self.permute_r(result, nums, k)

        return result

    def permute_r(self, result, nums, k):
        if k == 1:
            # copy这里精髓了
            result.append(nums.copy())

        for i in range(k):
            nums[i], nums[k-1] = nums[k-1], nums[i]
            self.permute_r(result, nums, k-1)
            nums[i], nums[k-1] = nums[k-1], nums[i]


if __name__ == "__main__":
    sl = Solution()
    nums = [1, 2, 3]
    print(sl.permute(nums))