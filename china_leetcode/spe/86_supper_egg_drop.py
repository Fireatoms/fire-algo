# link: https://leetcode-cn.com/problems/super-egg-drop/


class Solution:
    def __init__(self):
        self.memo = {}

    def superEggDrop(self, K: int, N: int) -> int:
        return self.dp(K, N)

    def dp(self, k, n):
        if (k, n) in self.memo:
            return self.memo[k, n]
        if n <= 0:
            return 0
        elif k == 1:
            return n
        else:
            low, high = 1, n
            while low + 1 < high:
                mid = low + (high - low) // 2
                t1 = self.dp(k - 1, mid - 1)
                t2 = self.dp(k, n - mid)
                if t1 < t2:
                    low = mid + 1
                elif t1 > t2:
                    high = mid - 1
                else:
                    low = high = mid

            ans = 1 + min(max(self.dp(k - 1, mid - 1), self.dp(k, n - mid)) for mid in (low, high))

        self.memo[k, n] = ans
        return ans
