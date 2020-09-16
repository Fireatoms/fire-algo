# link: https://leetcode.com/problems/count-of-smaller-numbers-after-self/
from typing import List


class Solution:
    def __init__(self):
        self.ans = []

    def countSmaller(self, nums: List[int]) -> List[int]:
        indexes = [i for i in range(len(nums))]
        self.ans = [0] * len(nums)
        self.merge_sort(nums, indexes, 0, len(nums) - 1)
        return self.ans

    def merge_sort(self, nums, indexes, p, r):
        if p >= r:
            return

        q = p + (r - p) // 2
        self.merge_sort(nums, indexes, p, q)
        self.merge_sort(nums, indexes, q + 1, r)
        self.merge_update_ans(nums, indexes, p, q, r)

    def merge_update_ans(self, nums, indexes, p, q, r):
        nums_tmp = [0] * (r - p + 1)
        indexes_tmp = [0] * (r - p + 1)
        i, j, k = p, q + 1, 0

        while i <= q and j <= r:
            if nums[i] <= nums[j]:
                nums_tmp[k] = nums[i]
                indexes_tmp[k] = indexes[i]
                self.ans[indexes[i]] += j - q - 1
                i += 1
            else:
                nums_tmp[k] = nums[j]
                indexes_tmp[k] = indexes[j]
                j += 1
            k += 1

        while i <= q:
            nums_tmp[k] = nums[i]
            indexes_tmp[k] = indexes[i]
            self.ans[indexes[i]] += r - q
            i += 1
            k += 1

        while j <= r:
            nums_tmp[k] = nums[j]
            indexes_tmp[k] = indexes[j]
            j += 1
            k += 1

        nums[p:r+1] = nums_tmp[:]
        indexes[p:r+1] = indexes_tmp[:]


if __name__ == "__main__":
    nums = [5, 2, 6, 1]
    sl = Solution()
    print(sl.countSmaller(nums))