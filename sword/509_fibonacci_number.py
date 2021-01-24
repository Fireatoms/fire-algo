# link: https://leetcode-cn.com/problems/fibonacci-number/


class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        prepre, pre, cur = 0, 1, 1
        for i in range(2, n + 1):
            cur = prepre + pre
            prepre = pre
            pre = cur
        return cur

    def fib_dp(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0] * (n + 1)
        dp[0], dp[1] = 0, 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def fib_recur(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib_recur(n - 1) + self.fib_recur(n - 2)

    def fib_recur_mem(self, n: int) -> int:
        mem = {}
        def fib_r(n):
            if n < 2:
                mem[n] = n
                return n
            if n in mem:
                return mem[n]
            ans = fib_r(n - 1) + fib_r(n - 2)
            mem[n] = ans
            return ans
        return fib_r(n)


if __name__ == "__main__":
    sl = Solution()
    print(sl.fib_recur(3))
    print(sl.fib_recur_mem(3))