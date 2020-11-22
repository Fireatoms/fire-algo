# link: https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op_map = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x/y)
        }
        for t in tokens:
            if t not in op_map:
                stack.append(int(t))
            else:
                b, a = stack.pop(), stack.pop()
                stack.append(op_map[t](a, b))

        return stack[0]

    def evalRPNNormal(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t.isdigit() or (t[0] == "-" and t[1:].isdigit()):
                stack.append(int(t))
            else:
                b, a = stack.pop(), stack.pop()
                if t == "+":
                    res = a + b
                elif t == "-":
                    res = a - b
                elif t == "*":
                    res = a * b
                else:
                    res = int(a / b)
                stack.append(res)
        return stack[0]

if __name__ == "__main__":
    print("a".isdigit())
    print(ord("a"))
    stack = [1, 2, 3]
    a, b = stack.pop(), stack.pop()
    print(a, b)
