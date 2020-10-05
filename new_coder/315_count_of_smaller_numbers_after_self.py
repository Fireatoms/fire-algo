# link: https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/


class Solution:
    def __init__(self):
        self.ans = []

    def countSmaller(self, nums: List[int]) -> List[int]:
        length = len(nums)
        index_of_nums = [i for i in range(length)]
        self.ans = [0] * length
        self.merge_sort(nums, index_of_nums, 0, length - 1)
        return self.ans

    def merge_sort(self, nums, index_of_nums, p, r):
        if p >= r:
            return

        q = p + (r - p) // 2
        self.merge_sort(nums, index_of_nums, p, q)
        self.merge_sort(nums, index_of_nums, q + 1, r)
        self.merge(nums, index_of_nums, p, q, r)

    def merge(self, nums, index_of_nums, p, q, r):
        nums_tmp = [0] * (r - p + 1)
        index_of_nums_tmp = [0] * (r - p + 1)

        i, j, k = p, q + 1, 0
        while i <= q and j <= r:
            if nums[i] > nums[j]:
                nums_tmp[k] = nums[j]
                index_of_nums_tmp[k] = index_of_nums[j]
                j += 1
            else:
                nums_tmp[k] = nums[i]
                index_of_nums_tmp[k] = index_of_nums[i]
                self.ans[index_of_nums[i]] += j - q - 1
                i += 1
            k += 1

        while i <= q:
            nums_tmp[k] = nums[i]
            index_of_nums_tmp[k] = index_of_nums[i]
            self.ans[index_of_nums[i]] += r - q
            i += 1
            k += 1

        while j <= r:
            nums_tmp[k] = nums[j]
            index_of_nums_tmp[k] = index_of_nums[j]
            j += 1
            k += 1

        nums[p:r+1] = nums_tmp
        index_of_nums[p:r+1] = index_of_nums_tmp