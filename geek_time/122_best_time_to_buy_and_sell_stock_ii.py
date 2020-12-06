# link: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        max_profit = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i+1]:
                i += 1
            valley = i
            while i < len(prices) - 1 and prices[i] <= prices[i+1]:
                i += 1
            peak = i
            max_profit += max(0, prices[peak] - prices[valley])
        return max_profit

    def maxProfitOnePass(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]

        return max_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    sl = Solution()
    print(sl.maxProfit(prices))