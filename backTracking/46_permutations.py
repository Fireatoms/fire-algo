# link: https://leetcode.com/problems/permutations/
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = k = len(nums)
        self.permute_r(result, nums, n, k)

        return result

    def permute_r(self, result, nums, n, k):
        if k == 1:
            # copy这里精髓了
            result.append(nums.copy())

        for i in range(k):
            tmp = nums[i]
            nums[i] = nums[k-1]
            nums[k-1] = tmp

            self.permute_r(result, nums, n, k-1)

            # 复原，也可以直接使用最上面的交换命令再操作一遍
            # tmp = nums[i]
            # nums[i] = nums[k - 1]
            # nums[k - 1] = tmp
            nums[k-1] = nums[i]
            nums[i] = tmp


if __name__ == "__main__":
    sl = Solution()
    nums = [1, 2, 3]
    print(sl.permute(nums))