# link: https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        s_len = len(s)

        for v in t:
            if s_pointer >= s_len:
                return True
            if v == s[s_pointer]:
                s_pointer += 1

        return s_pointer >= s_len


class Solution1:
    def isSubsequence(self, s: str, t: str) -> bool:
        """more elegant two pointer"""
        ps = pt = 0

        while ps < len(s) and pt < len(t):
            if s[ps] == t[pt]:
                ps += 1
            pt += 1

        return ps >= len(s)


class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = iter(t)
        return all(v in t for v in s)


if __name__ == "__main__":
    sl = Solution()
    print(sl.isSubsequence('acd', 'acaaabd'))