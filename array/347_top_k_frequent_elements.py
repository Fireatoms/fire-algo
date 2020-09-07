# link: https://leetcode.com/problems/top-k-frequent-elements/
import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        count_heap = []
        for i, v in count.items():
            heapq.heappush(count_heap, (-v, i))

        k_large = heapq.nsmallest(k, count_heap)
        return [v[1] for v in k_large]

    def topKFrequentPython(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)

        # print(count.keys())
        # print(count.get(1))



if __name__ == "__main__":
    arr = [1,1,1,2,2,2,3]
    sl = Solution()
    sl.topKFrequentPython(arr, 2)