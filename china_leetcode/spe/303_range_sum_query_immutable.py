# link: https://leetcode-cn.com/problems/range-sum-query-immutable/


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums_sum = self.calculate_nums_sum(nums)

    def calculate_nums_sum(self, nums):
        length = len(nums)
        nums_sum = [0] * (length + 1)
        for i in range(1, length + 1):
            nums_sum[i] = nums_sum[i - 1] + nums[i - 1]
        return nums_sum

    def sumRange(self, i: int, j: int) -> int:
        return self.nums_sum[j + 1] - self.nums_sum[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)