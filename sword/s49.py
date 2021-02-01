# link: https://leetcode-cn.com/problems/chou-shu-lcof/


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp, a, b, c = [1] * n, 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = 2 * dp[a], 3 * dp[b], 5 * dp[c]
            dp[i] = min(n2, n3, n5)
            if n2 == dp[i]: a += 1
            if n3 == dp[i]: b += 1
            if n5 == dp[i]: c += 1
        return dp[-1]