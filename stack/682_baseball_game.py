# link: https://leetcode.com/problems/baseball-game/
from typing import List

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for ch in ops:
            if ch.lstrip('-').isdigit():
                stack.append(int(ch))
            elif ch == 'C':
                stack.pop()
            elif ch == 'D':
                stack.append(2 * stack[-1])
            elif ch == '+':
                stack.append(stack[-1] + stack[-2])

        return sum(stack)


if __name__ == "__main__":
    sl = Solution()
    r = sl.calPoints(["5","-2","4","C","D","9","+","+"])
    print(r)