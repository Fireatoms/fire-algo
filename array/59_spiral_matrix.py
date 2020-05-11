# link: https://leetcode.com/problems/spiral-matrix-ii/


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n <= 0:
            return []

        ret = [[None for _ in range(n)] for _ in range(n)]
        left, right, up, down, num = 0, n-1, 0, n-1, 1

        while left <= right and up <= down:
            for i in range(left, right+1):
                ret[up][i] = num
                num += 1
            up += 1

            for i in range(up, down+1):
                ret[i][right] = num
                num += 1
            right -= 1

            for i in range(right, left-1, -1):
                ret[down][i] = num
                num += 1
            down -= 1

            # for i in range(down, up+1): 从下往上啊，这写的是个啥，这错误实在低级
            for i in range(down, up-1, -1):
                ret[i][left] = num
                num += 1
            left += 1

        return ret
