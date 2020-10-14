# link: https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/
from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        length_A, length_B = len(A), len(B)
        ans = 0
        dp = [[0] * (length_B + 1) for _ in range(length_A + 1)]

        for i in range(1, length_A + 1):
            for j in range(1, length_B + 1):
                dp[i][j] = dp[i-1][j-1] + 1 if A[i-1] == B[j-1] else 0
                ans = max(ans, dp[i][j])

        return ans

    def findLengthWindow(self, A: List[int], B: List[int]) -> int:
        length_A, length_B = len(A), len(B)
        ans = 0
        for i in range(length_A):
            sub_length = min(length_A - i, length_B)
            ans = max(ans, self.max_repeated_length(A, B, i, 0, sub_length))

        for j in range(length_B):
            sub_length = min(length_A, length_B - j)
            ans = max(ans, self.max_repeated_length(A, B, 0, j, sub_length))

        return ans

    def max_repeated_length(self, list_a, list_b, i, j, length):
        max_length, k = 0, 0
        for l in range(length):
            if list_a[l + i] == list_b[l + j]:
                k += 1
                max_length = max(max_length, k)
            else:
                # wrong: because the loop may terminate when we get the max_length
                # max_length = max(max_length, k)
                k = 0

        return max_length


if __name__ == "__main__":
    A = [1,2,3,2,1]
    B = [3,2,1,4,7]
    sl = Solution()
    print(sl.findLengthWindow(A, B))