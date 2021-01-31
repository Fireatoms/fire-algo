# link: https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/solution/zui-xiao-de-kge-shu-by-leetcode-solution/
from typing import List
import heapq
import random


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k <= 0:
            return []
        self.quick_sort(arr, k, 0, len(arr) - 1)
        return arr[:k]

    def quick_sort(self, arr, k, p, r):
        if p >= r:
            return
        q = self.partition(arr, p, r)
        if q > k - 1:
            self.quick_sort(arr, k, p, q - 1)
        if q < k - 1:
            self.quick_sort(arr, k, q + 1, r)

    def partition(self, arr, p, q):
        rand_idx = random.randint(p, q)
        arr[q], arr[rand_idx] = arr[rand_idx], arr[q]
        i, j = p, p
        while j < q:
            if arr[j] < arr[q]:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
            j += 1
        arr[i], arr[q] = arr[q], arr[i]
        return i

    def getLeastNumbersHeap(self, arr: List[int], k: int) -> List[int]:
        ans = []
        if k <= 0:
            return ans
        for v in arr:
            if len(ans) < k:
                heapq.heappush(ans, -v)
            else:
                if v < -ans[0]:
                    heapq.heappop(ans)
                    heapq.heappush(ans, -v)
        return [-v for v in ans]


if __name__ == "__main__":
    sl = Solution()
    nums = [0,2,0,5]
    print(sl.getLeastNumbers(nums, 3))
