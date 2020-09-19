# link: https://leetcode.com/problems/longest-common-prefix/
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        min_length, ans = len(strs[0]), ''
        for str in strs:
            min_length = min(min_length, len(str))

        for i in range(min_length):
            cur_str = strs[0][i]
            common = True
            for str in strs:
                if str[i] != cur_str:
                    common = False
                    break

            if common:
                ans += cur_str
            else:
                break

        return ans

    def longestCommonPrefixVertical(self, strs: List[str]) -> str:
        # perfect
        if not strs:
            return ''

        for i in range(len(strs[0])):
            cur_str = strs[0][i]
            for j in range(1, len(strs)):
                if len(strs[j]) == i or strs[j][i] != cur_str:
                    return strs[0][:i]

        return strs[0]


if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    sl = Solution()
    print(sl.longestCommonPrefix(strs))