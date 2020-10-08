# link: https://leetcode-cn.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        valid_pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []
        for c in s:
            if c in valid_pairs:
                stack.append(c)
            else:
                if stack and valid_pairs[stack.pop()] == c:
                    continue
                else:
                    return False

        return not stack