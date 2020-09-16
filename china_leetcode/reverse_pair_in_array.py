# link: https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/
from typing import List


class Solution:
    def __init__(self):
        self.num = 0

    def reversePairs(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        self.merge_sort(nums, 0, len(nums) - 1)
        return self.num

    def merge_sort(self, nums, p, r):
        if p >= r:
            return

        q = p + (r - p) // 2
        self.merge_sort(nums, p, q)
        self.merge_sort(nums, q + 1, r)
        self.merge(nums, p, q, r)

    def merge(self, nums, p, q, r):
        tmp = [0] * (r - p + 1)
        # i, j, k, = 0, q + 1, 0 shame！
        i, j, k, = p, q + 1, 0

        while i <= q and j <= r:
            if nums[i] <= nums[j]:
                tmp[k] = nums[i]
                i += 1
            else:
                self.num += q - i + 1
                tmp[k] = nums[j]
                j += 1
            k += 1

        if i <= q:
            tmp[k:] = nums[i:q + 1]

        if j <= r:
            tmp[k:] = nums[j:r + 1]

        nums[p:r+1] = tmp[:]


if __name__ == "__main__":
    nums = [7, 5, 6, 4]
    sl = Solution()
    print(sl.reversePairs(nums))