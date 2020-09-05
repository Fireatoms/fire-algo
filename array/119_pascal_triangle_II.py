# link: https://leetcode.com/problems/pascals-triangle-ii/


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pre_row = []
        row = [1]
        for i in range(rowIndex+1):
            row = [None for _ in range(i+1)]
            row[0], row[-1] = 1, 1
            for j in range(1, i):
                row[j] = pre_row[j-1] + pre_row[j]
            pre_row = row
        return row

    def getRowLowSpaceConsumption(self, rowIndex: int) -> List[int]:
        row = [1 for _ in range(rowIndex+1)]
        for i in range(rowIndex+1):
            row[i] = 1
            for j in range(i-1, 0, -1):
                row[j] = row[j] + row[j-1]

        return row