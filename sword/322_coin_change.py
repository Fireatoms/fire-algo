# link: https://leetcode-cn.com/problems/coin-change/
from typing import List


class Solution:
    def coinChangeMemo(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(n):
            min_num = float("inf")
            if n in memo: return memo[n]
            if n == 0: return 0
            if n < 0: return -1
            for coin in coins:
                sub_problem = dp(n - coin)
                if sub_problem == -1: continue
                min_num = min(min_num, sub_problem + 1)

            memo[n] = min_num if min_num != float("inf") else -1
            return memo[n]
        return dp(amount)

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i - coin < 0: continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] < float("inf") else -1


if __name__ == "__main__":
    sl = Solution()
    coins = [1, 2, 5]
    amount = 11
    print(sl.coinChangeMemo(coins, amount))
    print(sl.coinChange(coins, amount))