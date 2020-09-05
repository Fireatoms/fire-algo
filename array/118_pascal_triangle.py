# link: https://leetcode.com/problems/pascals-triangle/


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        if numRows == 1: return [[1]]

        res = [[1]]
        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                row.append(res[i-1][j-1] + res[i-1][j])
            row.append(1)
            res.append(row)

        return res

    def generate_dp(self, numRows: int) -> List[List[int]]:
        tri = []

        for i in range(numRows):
            row = [None for _ in range(i+1)]
            row[0], row[-1] = 1, 1

            for j in range(1, i):
                # i >= 2 guarantees tri[i] exists
                row[j] = tri[i-1][j-1] + tri[i-1][j]

            tri.append(row)

        return tri