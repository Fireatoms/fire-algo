# link: https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/


class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        prepre, pre, cur = 0, 1, 0
        for i in range(2, n + 1):
            cur = prepre + pre
            prepre = pre
            pre = cur
        return cur % 1000000007


if __name__ == "__main__":
    sl = Solution()
    print(sl.fib(3))