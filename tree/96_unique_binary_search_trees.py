# link: https://leetcode.com/problems/unique-binary-search-trees/
# https://blog.csdn.net/u010853261/article/details/54969599

class Solution:
    # dp: f(i) = f(0)*f(i-1) + f(1)*f(i-2) + .. + f(i-1)*f(0)
    def numTrees(self, n: int) -> int:
        f = [0] * (n+1)
        f[0] = f[1] = 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                f[i] += f[j-1] * f[i-j]

        return f[n]
