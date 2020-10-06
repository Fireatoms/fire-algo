# link: https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/
import heapq


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        ans = []
        for i, v in enumerate(arr):
            if i < k:
                heapq.heappush(ans, -v)
                continue
            heapq.heappushpop(ans, -v)

        return [-v for v in ans]