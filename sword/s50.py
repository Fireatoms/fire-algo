# link: https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/


class Solution:
    def firstUniqChar(self, s: str) -> str:
        assist_dict = {}
        for sv in s:
            assist_dict[sv] = assist_dict.get(sv, 0) + 1

        possible_set = set()
        for k, v in assist_dict.items():
            if v == 1:
                possible_set.add(k)

        for sv in s:
            if sv in possible_set:
                return sv

        return " "