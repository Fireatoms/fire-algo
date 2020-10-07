# link: https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/
from typing import List


class Solution:
    def findLengthBrute(self, A: List[int], B: List[int]) -> int:
        ans = 0
        for i in range(len(A)):
            for j in range(len(B)):
                k = 0
                while i + k < len(A) and j + k < len(B) and A[i+k] == B[j+k]:
                    k += 1
                ans = max(ans, k)

        return ans

    def findLength(self, A: List[int], B: List[int]) -> int:
        length_A, length_B, ans = len(A), len(B), 0
        dp = [[0] * (length_B + 1) for _ in range(length_A + 1)]

        for i in range(length_A - 1, -1, -1):
            for j in range(length_B - 1, -1, -1):
                dp[i][j] = dp[i+1][j+1] + 1 if A[i] == B[j] else 0
                ans = max(ans, dp[i][j])

        return ans



if __name__ == "__main__":
    A = [1, 2, 3, 2, 1]
    B = [3, 2, 1, 4, 7]
    sl = Solution()
    sl.findLengthBrute(A, B)