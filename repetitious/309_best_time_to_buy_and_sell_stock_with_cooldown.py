# link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        dp = [[0] * 3 for _ in range(len(prices))]
        dp[0][0] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])

        return max(dp[len(prices)-1][1], dp[len(prices)-1][2])