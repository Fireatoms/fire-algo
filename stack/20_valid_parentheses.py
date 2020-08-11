# link: https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        symbol_valid_pairs = {'{': '}', '[': ']', '(': ')'}
        left_symbol = ['{', '[', '(']
        right_symbol = ['}', ']', ')']
        symbol_stack = []

        for c in s:
            if c in left_symbol:
                symbol_stack.append(c)
            if c in right_symbol:
                if not symbol_stack or symbol_valid_pairs[symbol_stack.pop()] != c:
                    return False

        if symbol_stack:
            return False

        return True