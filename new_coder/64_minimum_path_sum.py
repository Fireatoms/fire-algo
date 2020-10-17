# link: https://leetcode-cn.com/problems/minimum-path-sum/


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row_length, column_length = len(grid), len(grid[0])
        dp = [[0] * column_length for _ in range(row_length)]

        dp[0][0] = grid[0][0]
        for i in range(1, row_length):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, column_length):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, row_length):
            for j in range(1, column_length):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[row_length-1][column_length-1]