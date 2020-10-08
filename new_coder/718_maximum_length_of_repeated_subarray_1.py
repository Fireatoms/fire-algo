# link: https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/


class Solution:
    def findLengthDp(self, A: List[int], B: List[int]) -> int:
        length_A, length_B = len(A), len(B)
        ans = 0
        dp = [[0] * (length_B + 1) for _ in range((length_A + 1))]

        for i in range(length_A - 1, -1, -1):
            for j in range(length_B - 1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = 0
                ans = max(ans, dp[i][j])

        return ans