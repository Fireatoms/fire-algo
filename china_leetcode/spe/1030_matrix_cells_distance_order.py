# link: https://leetcode-cn.com/problems/matrix-cells-in-distance-order/
# link: https://leetcode.com/problems/matrix-cells-in-distance-order/discuss/278746/Python-straightforward-DFS-and-BFS


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        bfs, res, memo = [(r0, c0)], [], {(r0, c0)}
        while bfs:
            res += bfs
            new_bfs = []
            for i, j in bfs:
                for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                    if 0 <= x < R and 0 <= y < C and (x, y) not in memo:
                        memo.add((x, y))
                        new_bfs.append((x, y))

            bfs = new_bfs

        return res


# dfs
class SolutionDfs:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        def dfs(i, j):
            seen.add((i, j))
            res.append([i, j])
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < R and 0 <= y < C and (x, y) not in seen:
                    dfs(x, y)
        res, seen = [], set()
        dfs(r0, c0)
        return sorted(res, key = lambda x: abs(x[0] - r0) + abs(x[1] - c0))