# link: https://leetcode.com/problems/backspace-string-compare/


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.handle(S) == self.handle(T)

    def handle(self, s):
        stack = []
        for i in s:
            if i != '#':
                stack.append(i)
            else:
                if stack:
                    stack.pop()

        return ''.join(stack)