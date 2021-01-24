# link: https://leetcode-cn.com/problems/coin-change/
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if amount - coin < 0: continue
                dp[i] = min(dp[i - coin] + 1, dp[i])
        return -1 if dp[amount] == float("inf") else dp[amount]


if __name__ == "__main__":
    sl = Solution()
    coins = [1, 2, 5]
    amount = 11
    res = sl.coinChange(coins, amount)
    print(res)