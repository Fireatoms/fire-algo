# link: https://leetcode-cn.com/problems/sliding-window-maximum/
from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = deque()
        n = len(nums)

        def clean():
            if queue and queue[0] == i - k:
                queue.popleft()
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)

        for i in range(k):
            clean()
        res.append(nums[queue[0]])

        for i in range(k, n):
            clean()
            res.append(nums[queue[0]])

        return res

    def maxSlidingWindowSimplify(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = deque()
        n = len(nums)
        for i in range(n):
            if queue and queue[0] == i - k:
                queue.popleft()
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
            if i < k - 1:
                continue
            res.append(nums[queue[0]])

        return res

    def maxSlidingWindowBrute(self, nums: List[int], k: int) -> List[int]:
        return [max(nums[i:i+k]) for i in range(len(nums)-k+1)]


if __name__ == "__main__":
    # nums = [1, 3, -1, -3, 5, 3, 6, 7]
    nums = [1, 3, -3, 4, 1, 3, 2]
    sl = Solution()
    print(sl.maxSlidingWindow(nums, 3))