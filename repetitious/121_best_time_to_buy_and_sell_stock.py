# link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
    def maxProfitBrute(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                cur_profit = prices[j] - prices[i]
                max_profit = max(max_profit, cur_profit)

        return max_profit

    def maxProfitDp(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = prices[0]
        dp[0][1] = 0

        for i in range(1, len(prices)):
            dp[i][0] = min(dp[i-1][0], prices[i])
            dp[i][1] = max(dp[i-1][1], prices[i] - dp[i-1][0])

        return dp[len(prices)-1][1]

    def maxProfitDpImprove(self, prices: List[int]) -> int:
        ans, dp = 0, 0
        for i in range(1, len(prices)):
            cur_profit = prices[i] - prices[i-1]
            dp = max(cur_profit, dp + cur_profit)
            ans = max(ans, dp)

        return ans

    def maxProfit(self, prices: List[int]) -> int:
        ans, min_price = 0, float('inf')
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                ans = max(ans, prices[i] - min_price)

        return ans


if __name__ == "__main__":
    sl = Solution()
    prices = [7,1,5,3,6,4]
    print(sl.maxProfitDp(prices))