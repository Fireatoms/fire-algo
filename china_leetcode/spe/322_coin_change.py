# link: https://leetcode-cn.com/problems/coin-change/
from typing import List
from functools import lru_cache


class Solution:
    def __init__(self):
        self.cache = {}
        self.coins = []

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0

        return self.dp(amount, coins)

    def dp(self, amount, coins):
        if amount < 0: return -1
        if amount == 0: return 0

        if amount in self.cache:
            return self.cache[amount]

        min_num = float('inf')
        for coin in coins:
            res = self.dp(amount - coin, coins)
            if 0 <= res < min_num:
                min_num = res + 1

        if min_num < float('inf'):
            self.cache[amount] = min_num
        else:
            self.cache[amount] = -1
            min_num = -1
        return min_num

    def coinChangeDp(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1




if __name__ == "__main__":
    coins = [186,419,83,408]
    target = 6279
    sl = Solution()
    print(sl.coinChange(coins, target))