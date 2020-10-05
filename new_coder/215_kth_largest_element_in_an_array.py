# link: https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
import heapq
import random


class Solution:
    def __init__(self):
        self.ans = 0

    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.quick_sort_r(nums, 0, len(nums) - 1, k)
        return self.ans

    def quick_sort_r(self, nums, p, r, k):
        if p > r:
            return

        q = self.partition(nums, p, r)
        if q + 1 == k:
            self.ans = nums[q]
            return
        elif q + 1 > k:
            self.quick_sort_r(nums, p, q - 1, k)
        else:
            self.quick_sort_r(nums, q + 1, r, k)

    def partition(self, nums, p, r):
        i = j = p
        pivot_idx = random.randint(p, r)
        nums[r], nums[pivot_idx] = nums[pivot_idx], nums[r]
        pivot = nums[r]

        while i < r:
            if nums[i] > pivot:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            i += 1

        nums[j], nums[r] = nums[r], nums[j]
        return j

    def findKthLargestHeap(self, nums: List[int], k: int) -> int:
        heap_assist = []
        for num in nums:
            if len(heap_assist) < k:
                heapq.heappush(heap_assist, num)
            else:
                heapq.heappushpop(heap_assist, num)

        return heap_assist[0]