# link: https://leetcode-cn.com/problems/longest-valid-parentheses/


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right, max_length = 0, 0, 0
        for sv in s:
            if sv == "(":
                left += 1
            else:
                right += 1
            if left == right:
                max_length = max(max_length, 2 * left)
            elif right > left:
                left, right = 0, 0

        left, right = 0, 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                max_length = max(max_length, 2*left)
            elif left > right:
                left, right = 0, 0

        return max_length

    def longestValidParenthesesStack(self, s: str) -> int:
        s_len = len(s)
        stack = [-1]
        max_length = 0
        for i in range(s_len):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    max_length = max(max_length, i-stack[-1])
                else:
                   stack.append(i)
        return max_length

    def longestValidParenthesesDfs(self, s: str) -> int:
        s_len = len(s)
        dp = [0] * s_len
        max_length = 0
        for i in range(1, s_len):
            if s[i] == ")":
                if s[i-1] == "(":
                    if i - 2 >= 0:
                        dp[i] = dp[i-2] + 2
                    else:
                        dp[i] = 2
                elif i - dp[i-1] - 1 >= 0 and s[i-dp[i-1]-1] == "(":
                    if i - dp[i-1] - 2 >= 0:
                        dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
                    else:
                        dp[i] = dp[i-1] + 2
            max_length = max(dp[i], max_length)
        return max_length

    def is_valid(self, s):
        valid_pairs = {")": "("}
        stack = []
        for i in s:
            if i not in valid_pairs:
                stack.append(i)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top != valid_pairs[i]:
                    return False

        return not stack

    def longestValidParenthesesBrute(self, s: str) -> int:
        s_len = len(s)
        init_length = s_len if s_len % 2 == 0 else s_len - 1
        for i in range(init_length, -1, -2):
            for j in range(s_len+1-i):
                if self.is_valid(s[j:j+i]):
                    return i


if __name__ == "__main__":
    sl = Solution()
    print(sl.longestValidParentheses("(())()()("))