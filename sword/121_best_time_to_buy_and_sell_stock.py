# link: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float("inf")
        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        return max_profit


if __name__ == "__main__":
    sl = Solution()
    prices = [7,1,5,3,6,4]
    print(sl.maxProfit(prices))