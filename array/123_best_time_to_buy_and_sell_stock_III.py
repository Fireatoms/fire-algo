# link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
# reference: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/794633/Python-O(n)-solution-with-optimization-explained
# not easy to understand


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        n, k = len(prices), 2

        prices_diff = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]
        if k > len(prices) // 2: return sum(diff for diff in prices_diff if diff > 0)

        # prices_diff = [prices[i] - prices[i-1] for i in range(1, len(prices))]
        # dp[0][0] = 0, mp[0][0] = 0
        dp = [[0] * (k+1) for _ in range(n-1)]
        mp = [[0] * (k+1) for _ in range(n-1)]

        dp[0][1], mp[0][1] = prices_diff[0], prices_diff[0]
        for i in range(1, n-1):
            for j in range(1, k+1):
                dp[i][j] = max(dp[i-1][j], mp[i-1][j-1]) + prices_diff[i]
                mp[i][j] = max(dp[i][j], mp[i-1][j])

        return max(mp[-1])