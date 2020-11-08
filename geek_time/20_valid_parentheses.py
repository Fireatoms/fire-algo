# link: https://leetcode-cn.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        valid_pairs = {
            "]": "[",
            "}": "{",
            ")": "("
        }

        stack = []
        for c in s:
            if c not in valid_pairs:
                stack.append(c)
            elif not stack or valid_pairs[c] != stack.pop():
                return False

        return not stack