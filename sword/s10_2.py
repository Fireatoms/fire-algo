# link: https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/


class Solution:
    def numWays(self, n: int) -> int:
        if n <= 1:
            return 1
        prepre, pre, cur = 1, 1, 0
        for i in range(1, n):
            cur = prepre + pre
            prepre = pre
            pre = cur

        return cur % 1000000007