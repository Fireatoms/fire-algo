# link: https://leetcode.com/problems/last-stone-weight/
from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """取反生成的小顶堆相当于原值的大顶堆"""
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            new_stone = heapq.heappop(stones) - heapq.heappop(stones)
            if new_stone != 0:
                heapq.heappush(stones, new_stone)

        res = 0
        if len(stones) > 0:
            res = -stones[0]

        return res


if __name__ == "__main__":
    sl = Solution()
    stones = [2, 2]
    res = sl.lastStoneWeight(stones)
    print(res)