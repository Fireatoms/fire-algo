# link: https://leetcode-cn.com/problems/n-queens-ii/


class Solution:
    def __init__(self):
        self.ans = 0
        self.column = set()
        self.left_diagonal = set()
        self.right_diagonal = set()

    def totalNQueens(self, n: int) -> int:
        self.backtracking(0, n)
        return self.ans

    def backtracking(self, row, n):
        if row == n:
            self.ans += 1
            return

        for i in range(n):
            if i in self.column or row + i in self.left_diagonal or row - i in self.right_diagonal:
                continue
            self.column.add(i)
            self.left_diagonal.add(row+i)
            self.right_diagonal.add(row-i)
            self.backtracking(row+1, n)
            self.column.remove(i)
            self.left_diagonal.remove(row+i)
            self.right_diagonal.remove(row-i)


if __name__ == "__main__":
    sl = Solution()
    print(sl.totalNQueens(3))