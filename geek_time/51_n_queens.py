# link: https://leetcode-cn.com/problems/n-queens/
from typing import List

class Solution:
    def __init__(self):
        self.res = []

    def is_ok(self, order, row, n):
        column = order[row]
        left_up = column - 1
        right_up = column + 1
        for i in range(row - 1, -1, -1):
            if order[i] == column:
                return False
            if left_up >= 0 and left_up == order[i]:
                return False
            if right_up < n and right_up == order[i]:
                return False
            left_up -= 1
            right_up += 1
        return True

    def convert(self, arr):
        res = []
        l = len(arr)
        for a in arr:
            s = ""
            for i in range(l):
                if a == i:
                    s += "Q"
                else:
                    s += "."
            res.append(s)
        return res

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.solve_queens_recur([-1] * n, 0, n)
        return self.res

    def solve_queens_recur(self, queen_order, row, n):
        if row == n:
            self.res.append(self.convert(queen_order))
            return

        for i in range(n):
            queen_order[row] = i
            if self.is_ok(queen_order, row, n):
                self.solve_queens_recur(queen_order, row+1, n)
            queen_order[row] = 0


class Solution1:
    def __init__(self):
        self.ans = []
        self.column = set()
        self.left_diagonal = set()
        self.right_diagonal = set()
        self.queen = []
        self.row = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.queen = [-1] * n
        self.row = ["."] * n
        self.backtracking(0, n)
        return self.ans

    def build_ans(self):
        one_ans = []
        for c in self.queen:
            self.row[c] = "Q"
            one_ans.append("".join(self.row))
            self.row[c] = "."
        self.ans.append(one_ans)

    def backtracking(self, row, n):
        if row == n:
            self.build_ans()
            return

        for i in range(n):
            if i in self.column or row + i in self.left_diagonal or row - i in self.right_diagonal:
                continue
            self.column.add(i)
            self.left_diagonal.add(row+i)
            self.right_diagonal.add(row-i)
            self.queen[row] = i
            self.backtracking(row+1, n)
            self.column.remove(i)
            self.left_diagonal.remove(row+i)
            self.right_diagonal.remove(row-i)


if __name__ == "__main__":
    sl = Solution1()
    print(sl.solveNQueens(4))