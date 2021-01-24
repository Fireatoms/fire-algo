# link: https://leetcode-cn.com/problems/maximal-square/
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        max_side = 0
        row, column = len(matrix), len(matrix[0])
        dp = [[0] * column for _ in range(row)]
        for i in range(row):
            for j in range(column):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                    max_side = max(max_side, dp[i][j])

        return max_side * max_side
