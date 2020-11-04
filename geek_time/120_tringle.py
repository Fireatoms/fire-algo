# link: https://leetcode-cn.com/problems/triangle/


class Solution:
    def minimumTotalDpSpace(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        # init
        dp = triangle[m - 1]

        for i in range(m - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]

        return dp[0]


    def minimumTotalDp(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = [[0] * m for _ in range(m)]
        # init the bottom layer
        dp[m - 1] = triangle[m - 1]

        for i in range(m - 2, -1, -1):
            for j in range(i+1):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]

        return dp[0][0]

    def __init__(self):
        self.memo = {}

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.minimumTotalRecur(triangle, 0, 0)

    def minimumTotalRecur(self, triangle, i, j):
        if i == len(triangle) - 1:
            return triangle[i][j]

        # if i == len(triangle) - 1:
        #     return triangle[i][j]

        if (i, j) in self.memo:
            return self.memo[(i, j)]

        res = min(
            self.minimumTotalRecur(triangle, i+1, j),
            self.minimumTotalRecur(triangle, i+1, j+1)
        ) + triangle[i][j]

        self.memo[(i, j)] = res
        return res