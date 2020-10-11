# link: https://www.nowcoder.com/questionTerminal/28c1dc06bc9b4afd957b01acdf046e69


class Solution:
    def min_deleted_nums(self, text):
        if not text:
            return

        return len(text) - self.longest_common_subsequence(text, text[::-1])

    def longest_common_subsequence(self, text1, text2):
        length1, length2 = len(text1), len(text2)
        dp = [[0] * (length2 + 1) for _ in range(length1 + 1)]

        for i in range(1, length1 + 1):
            for j in range(1, length2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]


if __name__ == "__main__":
    print(__name__)
    sl = Solution()
    print(sl.min_deleted_nums('abbacd'))
