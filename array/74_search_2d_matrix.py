#link: https://leetcode.com/problems/search-a-2d-matrix/
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        head_list = [matrix[i][0] for i in range(len(matrix))]
        row_index = self.last_le_index(head_list, target)

        if row_index == -1:
            return False

        return self.find_val(matrix[row_index], target)

    def last_le_index(self, l, val):
        low = 0
        high = len(l) - 1

        while low <= high:
            mid = (high - low) // 2 + low
            if l[mid] > val:
                high = mid - 1
            else:
                if mid == len(l) - 1 or l[mid + 1] > val:
                    return mid
                else:
                    low = mid + 1

        return -1

    def find_val(self, l, val):
        low = 0
        high = len(l) - 1

        while low <= high:
            mid = (high - low) // 2 + low
            if l[mid] > val:
                high = mid - 1
            elif l[mid] < val:
                low = mid + 1
            else:
                return True

        return False


if __name__ == "__main__":
    matrix = [[1]]
    target = 0
    sl = Solution()
    print(sl.searchMatrix(matrix, target))