# link: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            if prices[i+1] > prices[i]:
                max_profit += prices[i+1] - prices[i]
        return max_profit

    def maxProfitValley(self, prices: List[int]) -> int:
        max_profit, vally, peak, i = 0, 0, 0, 0
        prices_len = len(prices)
        while i < prices_len - 1:
            while i < prices_len - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = i
            while i < prices_len - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = i
            max_profit += prices[peak] - prices[valley]
        return max_profit


if __name__ == "__main__":
    sl = Solution()
    prices = [7,1,5,3,6,4]
    print(sl.maxProfit(prices))