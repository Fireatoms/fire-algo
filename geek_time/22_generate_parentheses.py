# link: https://leetcode-cn.com/problems/generate-parentheses/
from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def is_valid_parenthesis(self, parenthesis):
        stack = []
        valid_pairs = {
            ")": "("
        }
        for p in parenthesis:
            if p not in valid_pairs:
                stack.append(p)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if valid_pairs[p] != top:
                    return False

        return not stack

    def generateParenthesis(self, n: int) -> List[str]:
        self.get_parenthesis_recur(n, n, [])
        return self.res
        # return list(map(lambda x: "".join(x), self.res))

    def get_parenthesis_recur(self, left, right, parenthesis):
        if left == 0 and right == 0:
            # if self.is_valid_parenthesis(parenthesis):
            self.res.append("".join(parenthesis))
            return

        if left != 0:
            parenthesis.append("(")
            self.get_parenthesis_recur(left-1, right, parenthesis)
            parenthesis.pop()

        if right > left:
            parenthesis.append(")")
            self.get_parenthesis_recur(left, right-1, parenthesis)
            parenthesis.pop()




if __name__ == "__main__":
    sl = Solution()
    print(sl.generateParenthesis(3))