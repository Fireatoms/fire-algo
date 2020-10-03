class Solution:
    def numWays(self, n: int, k: int) -> int:
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            if i == 1:
                dp[i] = k
            elif i == 2:
                dp[i] = k * k
            else:
                dp[i] = dp[i - 1] * (k - 1) + dp[i - 2] * (k - 1)

        return dp[n]