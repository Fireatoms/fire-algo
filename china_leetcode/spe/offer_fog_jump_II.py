# link: https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/


class Solution:
    def numWays(self, n: int) -> int:
        if n == 0:
            return 1
        elif n <= 2:
            return n

        prepre, pre, cur = 1, 2, 0
        for i in range(3, n + 1):
            cur = prepre + pre
            prepre = pre
            pre = cur

        return cur % 1000000007