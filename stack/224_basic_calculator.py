# link: https://leetcode.com/problems/basic-calculator/


class Solution:
    def evaluate_expr(self, stack):
        res = stack.pop()
        while stack and stack[-1] != ')':
            sign = stack.pop()
            if sign == '-':
                res -= stack.pop()
            else:
                res += stack.pop()

        return res

    def calculate(self, s: str) -> int:
        stack = []
        # n: carry
        n, operand = 0, 0
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            if ch.isdigit():
                operand = (10 ** n * int(ch)) + operand
                n += 1
            elif ch != ' ':
                # push operand onto the stack
                if n:
                    stack.append(operand)
                    n, operand = 0, 0
                if ch == '(':
                    res = self.evaluate_expr(stack)
                    stack.pop()
                    stack.append(res)
                else:
                    stack.append(ch)

        if n:
            stack.append(operand)

        return self.evaluate_expr(stack)


class Solution1:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        sign = 1
        operand = 0
        for ch in s:
            if ch.isdigit():
                operand = 10 * operand + int(ch)
            elif ch == '-':
                res += operand * sign
                sign = -1
                operand = 0
            elif ch == '+':
                res += operand * sign
                sign = 1
                operand = 0
            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
                operand = 0
            elif ch == ')':
                res += operand * sign
                res *= stack.pop()
                res += stack.pop()
                operand = 0
                sign = 1

        res += operand * sign
        return res
    

if __name__ == "__main__":
    sl = Solution1()
    p = sl.calculate('7 - (1+2)+4')
    print(p)