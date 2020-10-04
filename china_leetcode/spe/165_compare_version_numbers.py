# link: https://leetcode-cn.com/problems/compare-version-numbers/


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        p1 = p2 = 0
        n1, n2 = len(version1), len(version2)

        while p1 < n1 or p2 < n2:
            chunk1, p1 = self.get_next_chunk(version1, p1, n1)
            chunk2, p2 = self.get_next_chunk(version2, p2, n2)
            if chunk1 != chunk2:
                return 1 if chunk1 > chunk2 else -1

        return 0

    def get_next_chunk(self, version, p, n):
        if p >= n:
            return 0, p
        end = p
        while end < len(version) and version[end] != '.':
            end += 1
        chunk = int(version[p:end])
        return chunk, end + 1