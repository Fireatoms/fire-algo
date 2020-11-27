# link: https://leetcode-cn.com/problems/valid-anagram/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list, t_list = [0] * 26, [0] * 26
        for i in s:
            s_list[ord(i) - ord("a")] += 1
        for i in t:
            t_list[ord(i) - ord("a")] += 1

        return s_list == t_list

    def isAnagramMap(self, s: str, t: str) -> bool:
        s_dict, t_dict = {}, {}
        for i in s:
            s_dict[i] = s_dict.get(i, 0) + 1
        for i in t:
            t_dict[i] = t_dict.get(i, 0) + 1

        return s_dict == t_dict
