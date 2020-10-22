# link: https://leetcode-cn.com/problems/triangle/


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = [[0] * m for _ in range(m)]
        dp[m - 1] = triangle[m - 1]

        for i in range(m - 2, -1, -1):
            for j in range(i + 1):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]

        return dp[0][0]

    def minimumTotalSpaceSaved(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = triangle[m - 1]

        for i in range(m - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]

        return dp[0]