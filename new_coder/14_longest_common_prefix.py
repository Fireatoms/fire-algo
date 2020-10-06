# link: https://leetcode-cn.com/problems/longest-common-prefix/


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if len(strs[j]) == i or strs[j][i] != strs[0][i]:
                    return strs[0][:i]

        return strs[0]