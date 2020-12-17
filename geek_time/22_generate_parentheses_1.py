# link: https://leetcode-cn.com/problems/generate-parentheses/
from typing import List


class Solution:
    def __init__(self):
        self.ans = []
        self.valid_parenthesis = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.generate_parenthesis_recur(n, n)
        return self.ans

    def generate_parenthesis_recur(self, left, right):
        if left == 0 and right == 0:
            self.ans.append("".join(self.valid_parenthesis))
            return

        if left > 0:
            self.valid_parenthesis.append("(")
            self.generate_parenthesis_recur(left-1, right)
            self.valid_parenthesis.pop()
        if right > left:
            self.valid_parenthesis.append(")")
            self.generate_parenthesis_recur(left, right-1)
            self.valid_parenthesis.pop()


if __name__ == "__main__":
    sl = Solution()
    print(sl.generateParenthesis(4))