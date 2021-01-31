# link: https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/
from typing import List


class Solution:
    def __init__(self):
        self.ans = []
        self.num = []

    def dfs(self, n_bit, n):
        if n_bit == n:
            self.ans.append("".join(self.num))
            return
        for i in range(10):
            self.num[n_bit] = str(i)
            self.dfs(n_bit + 1, n)

    def printNumbers(self, n: int) -> List[int]:
        self.num = ["0"] * n
        self.dfs(0, n)
        return self.ans


if __name__ == "__main__":
    sl = Solution()
    print(sl.printNumbers(3))