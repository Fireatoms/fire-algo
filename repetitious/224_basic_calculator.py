# link: https://leetcode.com/problems/basic-calculator/


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = 1
        res = 0
        operand = 0
        for ch in s:
            if ch.isdigit():
                operand = 10 * operand + int(ch)
            elif ch == '+':
                res += operand * sign
                sign = 1
                operand = 0
            elif ch == '-':
                res += operand * sign
                sign = -1
                operand = 0
            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
                operand = 0
            elif ch == ')':
                res += operand * sign
                res *= stack.pop()
                res += stack.pop()
                sign = 1
                operand = 0

        return res + operand * sign