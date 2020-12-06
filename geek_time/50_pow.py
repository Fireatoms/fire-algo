# link: https://leetcode-cn.com/problems/powx-n/


class Solution:
    def myPowIter(self, x: float, n: int) -> float:
        res = 1
        if n < 0:
            n = -n
            x = 1 / x
        while n:
            if n % 2:
                res *= x
                n -= 1
            else:
                x *= x
                n = n / 2
        return res

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0 :
            return self.myPow(1/x, -n)

        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x*x, n >> 1)


if __name__ == "__main__":
    sl = Solution()
    # print(sl.myPow(2, 5))
    print(sl.myPowIter(2, 5))