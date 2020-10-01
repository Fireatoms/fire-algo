# link: https://leetcode-cn.com/problems/climbing-stairs/


class Solution:
    def __init__(self):
        self.cache = {}

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prepre = 1
        pre = 2
        cur = 0
        for i in range(2, n):
            cur = prepre + pre
            prepre = pre
            pre = cur

        return cur

    def climbStairsRecur(self, n: int) -> int:
        if n <= 2:
            return n

        if n in self.cache:
            return self.cache[n]

        res = self.climbStairsRecur(n - 1) + self.climbStairsRecur(n - 2)
        self.cache[n] = res
        return res
    

if __name__ == "__main__":
    sl = Solution()
    print(sl.climbStairs(4))