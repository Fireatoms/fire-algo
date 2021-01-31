# link: https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/
from typing import List
import heapq
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        nums_len = len(nums)
        if nums_len == 0 or k == 0:
            return []
        ans = []
        assist_queue = deque()
        for i in range(k):
            while assist_queue and nums[assist_queue[-1]] <= nums[i]:
                assist_queue.pop()
            assist_queue.append(i)
        ans.append(nums[assist_queue[0]])

        for i in range(k, nums_len):
            while assist_queue and nums[assist_queue[-1]] <= nums[i]:
                assist_queue.pop()
            assist_queue.append(i)
            while assist_queue and assist_queue[0] <= i - k:
                assist_queue.popleft()
            ans.append(nums[assist_queue[0]])
        return ans

    def maxSlidingWindowHeap(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        nums_len = len(nums)
        assist_heap = [(-nums[i], i) for i in range(k)]
        heapq.heapify(assist_heap)
        ans = [-assist_heap[0][0]]
        for i in range(k, nums_len):
            heapq.heappush(assist_heap, (-nums[i], i))
            while assist_heap[0][1] <= i - k:
                heapq.heappop(assist_heap)
            ans.append(-assist_heap[0][0])
        return ans

    def maxSlidingWindowBrute(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        return [max(nums[i:i+k]) for i in range(n-k+1)]


if __name__ == "__main__":
    sl = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(sl.maxSlidingWindow(nums, k))
