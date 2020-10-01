# link: https://leetcode-cn.com/problems/product-of-array-except-self/
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left, right, ans = [0] * length, [0] * length, [0] * length

        left[0] = 1
        for i in range(1, length):
            left[i] = left[i - 1] * nums[i - 1]

        right[length - 1] = 1
        for i in range(length - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        for i in range(length):
            ans[i] = left[i] * right[i]

        return ans

    def productExceptSelfImprove(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0] * length

        ans[0] = 1
        for i in range(1, length):
            ans[i] = ans[i - 1] * nums[i - 1]

        right = 1
        for i in range(length - 1, -1, -1):
            ans[i] = ans[i] * right
            right *= nums[i]

        return ans


if __name__ == "__main__":
    nums = [1, 2, 3 ,4]
    sl = Solution()
    print(sl.productExceptSelfImprove(nums))