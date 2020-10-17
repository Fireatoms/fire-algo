# link: https://leetcode-cn.com/problems/is-subsequence/


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        length_s, length_t = len(s), len(t)
        i, j = 0, 0
        while j < length_t and i < length_s:
            if s[i] == t[j]:
                i += 1
            j += 1

        return i >= length_s


if __name__ == "__main__":
    s = 'axc'
    t = 'ahbgdc'
    sl = Solution()
    print(sl.isSubsequence(s, t))