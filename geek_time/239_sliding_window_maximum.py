# link: https://leetcode-cn.com/problems/sliding-window-maximum/
from typing import List
from collections import deque


class Solution:
    def maxSlidingWindowBrute(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        return [max(nums[i:i+k]) for i in range(n-k+1)]

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n * k == 0:
            return []

        queue = deque()
        res = []
        for i in range(n):
            self.clean(nums, i, k, queue)
            queue.append(i)
            if i < k - 1:
                continue
            res.append(nums[queue[0]])

        return res

    def clean(self, nums, i, k, queue):
        if queue and queue[0] == i - k:
            queue.popleft()

        while queue and nums[queue[-1]] < nums[i]:
            queue.pop()


if __name__ == "__main__":
    sl = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    print(sl.maxSlidingWindowBrute(nums, 3))
    print(sl.maxSlidingWindow(nums, 3))