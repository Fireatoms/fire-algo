# link: https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        rows = len(matrix)
        columns = len(matrix[0])
        top, bottom, left, right = 0, rows - 1, 0, columns - 1
        ans = []
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            for i in range(top + 1, bottom + 1):
                ans.append(matrix[i][right])
            if top < bottom and left < right:
                for i in range(right - 1, left - 1, -1):
                    ans.append(matrix[bottom][i])
                for i in range(bottom - 1, top, -1):
                    ans.append(matrix[i][left])
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        return ans


if __name__ == "__main__":
    sl = Solution()
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    print(sl.spiralOrder(matrix))