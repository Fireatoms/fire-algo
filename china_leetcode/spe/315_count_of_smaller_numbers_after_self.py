# link: https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/
from typing import List


class Solution:
    def __init__(self):
        self.ans = []

    def countSmaller(self, nums: List[int]) -> List[int]:
        length = len(nums)
        self.ans = [0] * length
        index_records = [i for i in range(length)]
        self.merge_sort(nums, index_records, 0, length - 1)
        return self.ans

    def merge_sort(self, nums, index_records, p, r):
        if p >= r:
            return

        q = (p + r) // 2
        self.merge_sort(nums, index_records, p, q)
        self.merge_sort(nums, index_records, q + 1, r)
        self.merge(nums, index_records, p, q, r)

    def merge(self, nums, index_records, p, q, r):
        nums_tmp = [0] * (r - p + 1)
        index_records_tmp = [0] * (r - p + 1)
        i, k, j = p, 0, q + 1

        while i <= q and j <= r:
            if nums[i] > nums[j]:
                nums_tmp[k] = nums[j]
                index_records_tmp[k] = index_records[j]
                j += 1
            else:
                nums_tmp[k] = nums[i]
                index_records_tmp[k] = index_records[i]
                self.ans[index_records[i]] += j - q - 1
                i += 1
            k += 1

            # if nums[i] > nums[j]:
            #     nums_tmp[k] = nums[j]
            #     index_records_tmp[k] = index_records[j]
            #     j += 1
            # else:
                  # error
            #     nums[k] = `nums[i]
            #     index_records_tmp[k] = index_records[i]
            #     # index_record records sorted index
            #     self.ans[index_records[i]] += j - q - 1
            #     i += 1
            # k += 1

        while i <= q:
            nums_tmp[k] = nums[i]
            index_records_tmp[k] = index_records[i]
            self.ans[index_records[i]] += r - q
            i += 1
            k += 1

        while j <= r:
            nums_tmp[k] = nums[j]
            index_records_tmp[k] = index_records[j]
            j += 1
            k += 1

        nums[p:r+1] = nums_tmp
        index_records[p:r+1] = index_records_tmp


if __name__ == "__main__":
    nums = [1, 2, 0]
    sl = Solution()
    print(sl.countSmaller(nums))