# link: https://leetcode-cn.com/problems/powx-n/


class Solution:
    def myPow(self, x: float, n: int) -> float:
        return self.myPow_r(x, n) if n > 0 else 1 / self.myPow_r(x, -n)

    def myPow_r(self, x, n):
        if n == 0:
            return 1
        y = self.myPow_r(x, n // 2)
        return y * y * x if n & 1 else y * y

    def myPowIter(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1

        return pow
