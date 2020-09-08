# link: https://leetcode.com/problems/kth-largest-element-in-an-array/
from typing import List
import random
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.res = 0
        self.quick_sort(nums, 0, len(nums)-1, k)
        return self.res

    def quick_sort(self, nums, p, r, k):
        # It must be checked when p == r, which is different from quick sorting
        if p > r:
            return

        q = self.partition(nums, p, r)
        if q + 1 == k:
            self.res = nums[q]
            return
        elif q + 1 > k:
            self.quick_sort(nums, p, q-1, k)
        else:
            self.quick_sort(nums, q+1, r, k)

    def partition(self, nums, p, r):
        i = p
        # optimization
        pivot_idx = random.randint(p, r)
        nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]
        pivot = nums[r]
        for j in range(p, r):
            if nums[j] > pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        nums[r], nums[i] = nums[i], nums[r]
        return i

    def findKthLargestHeap(self, nums: List[int], k: int) -> int:
        h = []
        for n in nums:
            if len(h) < k:
                heapq.heappush(h, n)
            else:
                heapq.heappushpop(h, n)
        return h[0]

if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    sl = Solution()
    # sl.findKthLargest(arr, 2)
    print(sl.findKthLargestHeap(arr, 3))
