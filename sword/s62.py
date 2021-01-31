# link: https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        ans = 0
        for i in range(2, n + 1):
            ans = (ans + m) % i
        return ans

    def lastRemainingRecur(self, n: int, m: int) -> int:
        if n == 0:
            return 0
        x = self.lastRemaining(n - 1, m)
        return (m + x) % n


if __name__ == "__main__":
    sl = Solution()
    print(sl.lastRemaining(5, 3))