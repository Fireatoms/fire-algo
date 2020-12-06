# link: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        for p in prices:
            if p < min_price:
                min_price = p
            else:
                max_profit = max(max_profit, p - min_price)
        return max_profit

    def maxProfitBrute(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            for j in range(i):
                max_profit = max(max_profit, prices[i]-prices[j])
        return max_profit


if __name__ == "__main__":
    sl = Solution()
    # prices = [7, 6, 4, 3, 1]
    prices = [7, 1, 5, 3, 6, 4]
    print(sl.maxProfit(prices))