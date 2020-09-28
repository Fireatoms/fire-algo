# link: https://leetcode-cn.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        valid_pairs = {'{': '}', '[': ']', '(': ')'}
        stack = []
        for sv in s:
            if sv in valid_pairs:
                stack.append(sv)
            else:
                if not stack or valid_pairs[stack[-1]] != sv:
                    return False
                stack.pop()

        return not stack