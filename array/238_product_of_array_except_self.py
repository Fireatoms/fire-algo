# link: https://leetcode.com/problems/product-of-array-except-self/


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_pro = [0] * len(nums)
        right_pro = [0] * len(nums)
        res = [0] * len(nums)
        left_pro[0] = 1
        right_pro[-1] = 1

        for i in range(n-1):
            left_pro[i+1] = nums[i] * left_pro[i]

        for j in range(n-1, 0, -1):
            right_pro[j-1] = right_pro[j] * nums[j]

        for i in range(n):
            res[i] = left_pro[i] * right_pro[i]

        return res

    def productExceptSelfLow(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0] * length

        ans[0] = 1
        for i in range(length-1):
            ans[i+1] = ans[i] * nums[i]

        r = 1
        for j in range(length-1, -1, -1):
            ans[j] *= r
            r *= nums[j]

        return ans