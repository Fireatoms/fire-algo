# link: https://leetcode-cn.com/problems/rearrange-string-k-distance-apart/
from collections import deque
import heapq


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        s_hash = {}
        for c in s:
            s_hash[c] = s_hash.get(c, 0) + 1

        queue_assist = deque()
        heap_assist = []
        ans = ''

        for key, val in s_hash.items():
            heapq.heappush(heap_assist, (-val, key))

        while heap_assist:
            val, key = heapq.heappop(heap_assist)
            ans += key
            val += 1
            queue_assist.append((val, key))
            if len(queue_assist) >= k:
                duplicate_val, duplicate_key = queue_assist.popleft()
                if duplicate_val != 0:
                    heapq.heappush(heap_assist, (duplicate_val, duplicate_key))

        return ans if len(s) == len(ans) else ''


if __name__ == "__main__":
    s = 'aabbcccc'
    k = 3
    sl = Solution()
    print(sl.rearrangeString(s, k))

