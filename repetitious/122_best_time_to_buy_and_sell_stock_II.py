# link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, max_profit = 0, 0
        valley, peak = prices[0], prices[0]
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]
            max_profit += peak - valley

        return max_profit

    def maxProfitImprove(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            if prices[i+1] > prices[i]:
                max_profit += prices[i+1] - prices[i]

        return max_profit