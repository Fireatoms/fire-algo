# link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) < 2 or k == 0:
            return 0
        n = len(prices)

        prices_diff = [prices[i] - prices[i-1] for i in range(1, len(prices))]
        if k > n // 2: return sum(pd for pd in prices_diff if pd > 0)

        dp = [[0] * (k+1) for _ in range(n-1)]
        mp = [[0] * (k+1) for _ in range(n-1)]
        dp[0][1] = prices_diff[0]
        mp[0][1] = prices_diff[0]

        for i in range(1, n-1):
            for j in range(1, k+1):
                dp[i][j] = max(mp[i-1][j-1], dp[i-1][j]) + prices_diff[i]
                mp[i][j] = max(dp[i][j], mp[i-1][j])

        return max(mp[-1])
