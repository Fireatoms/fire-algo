# link: https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/


class Solution:
    def numWays(self, n: int) -> int:
        if n == 0:
            return 1
        if n < 3:
            return n

        prepre = 1
        pre = 2
        cur = 0
        for i in range(3, n + 1):
            cur = prepre + pre
            prepre = pre
            pre = cur

        return cur % 1000000007