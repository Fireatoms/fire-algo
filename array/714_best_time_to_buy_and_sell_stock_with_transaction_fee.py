# link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0

        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])

        return dp[-1][0]

    def maxProfitImprove(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash

if __name__ == "__main__":
    sl = Solution()
    arr = [1,3,2,8,4,9]
    fee = 2
    print(sl.maxProfit(arr, 2))