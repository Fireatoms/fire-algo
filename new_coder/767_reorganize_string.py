# link: https://leetcode-cn.com/problems/reorganize-string/
import heapq
from collections import deque


class Solution:
    def reorganizeString(self, S: str) -> str:
        s_hash = {}
        for c in S:
            s_hash[c] = s_hash.get(c, 0) + 1

        heap_assist = []
        queue_assist = deque()
        ans = ''

        for key, val in s_hash.items():
            heapq.heappush(heap_assist, (-val, key))

        while heap_assist:
            val, key = heapq.heappop(heap_assist)
            ans += key
            val += 1
            queue_assist.append((val, key))
            if len(queue_assist) >= 2:
                duplicate_val, duplicate_key = queue_assist.popleft()
                if duplicate_val != 0:
                    heapq.heappush(heap_assist, (duplicate_val, duplicate_key))

        return ans if len(ans) == len(S) else ''