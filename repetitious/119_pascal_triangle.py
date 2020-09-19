# link: https://leetcode.com/problems/pascals-triangle-ii/


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pre_row = []
        cur_row = []
        for i in range(rowIndex+1):
            cur_row = [1] * (i + 1)
            cur_row[0], cur_row[-1] = 1, 1
            for j in range(1, i):
                cur_row[j] = pre_row[j-1] + pre_row[j]
            pre_row = cur_row
        return cur_row

    def getRowLow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)
        for i in range(rowIndex + 1):
            row[i] = 1
            for j in range(i-1, 0, -1):
                row[j] = row[j] + row[j-1]

        return row