# link: https://leetcode-cn.com/problems/is-subsequence/


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        length_s, length_t = len(s), len(t)
        while i < length_s and j < length_t:
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == length_s