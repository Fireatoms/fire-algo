# link: https://leetcode.com/problems/pascals-triangle/


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            dp = [1] * (i + 1)
            dp[0], dp[-1] = 1, 1
            for j in range(1, i):
                dp[j] = ans[i-1][j-1] + ans[i-1][j]
            ans.append(dp)
        return ans