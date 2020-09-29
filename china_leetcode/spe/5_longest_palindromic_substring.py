# link: https://leetcode-cn.com/problems/longest-palindromic-substring/


class Solution:
    def longestPalindromeBrute(self, s: str) -> str:
        length = len(s)

        max_len = 1
        start = 0

        for i in range(0, length - 1):
            for j in range(i + 1, length):
                if j - i + 1 > max_len and self.is_palindrome(i, j, s):
                    max_len = j - i + 1
                    start = i

        return s[start: start + max_len]

    def is_palindrome(self, i, j, s):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

    def longestPalindromeDp(self, s: str) -> str:
        length = len(s)
        dp = [[False] * length for _ in range(length)]
        max_len = 1
        start = 0

        for j in range(1, length):
            for i in range(j + 1):
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]

                if dp[i][j] and j - i + 1 > max_len:
                    start = i
                    max_len = j - i + 1

        return s[start: start + max_len]
