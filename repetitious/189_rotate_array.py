# link: https://leetcode.com/problems/rotate-array/


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        # Although the time-consuming is high, it is worthy to learn
        for i in range(k):
            pre = nums[-1]
            for j in range(len(nums)):
                nums[j], pre = pre, nums[j]

    def rotate_extra_arr(self, nums: List[int], k: int) -> None:
        extra = [0] * len(nums)
        for i in range(len(nums)):
            extra[(i+k)%len(nums)] = nums[i]
        nums[:] = extra

    def rotate_reverse(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)

    def reverse(self, nums, p, q):
        while p < q:
            nums[p], nums[q] = nums[q], nums[p]
            p += 1
            q -= 1
