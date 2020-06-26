# link: https://leetcode.com/problems/shortest-path-in-binary-matrix/
from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            # start cell is not empty
            return -1

        n = len(grid)
        visited = set()
        queue = deque()
        prev = {}

        visited.add((0, 0))
        queue.append((0, 0))
        prev[(0, 0)] = (-1, -1)

        while queue:
            ver = queue.popleft()
            for cell in self.get_adjacent_cells(ver, grid):
                if cell not in visited:
                    visited.add(cell)
                    prev[cell] = ver
                    if cell == (n-1, n-1):
                        return self.get_path_length(prev, (0, 0), (n-1, n-1))
                    queue.append(cell)

        if n == 1:
            # only one cell
            return 1
        return -1

    def get_path_length(self, prev, s, t):
        l = 1
        while t != s:
            l += 1
            t = prev[t]
        return l

    def get_adjacent_cells(self, ver, grid):
        cells = []
        n = len(grid)
        i = ver[0]
        j = ver[1]

        for x, y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
            if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                cells.append((x, y))

        return cells


if __name__ == "__main__":
    grid = [[0,0,1,0,0,0,0],[0,1,0,0,0,0,1],[0,0,1,0,1,0,0],[0,0,0,1,1,1,0],[1,0,0,1,1,0,0],[1,1,1,1,1,0,1],[0,0,1,0,0,0,0]]
    sl = Solution()
    print(sl.shortestPathBinaryMatrix(grid))

