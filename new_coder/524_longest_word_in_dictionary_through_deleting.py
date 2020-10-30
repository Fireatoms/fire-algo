# link: https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        res = ''
        for ds in d:
            if self.is_subsequence(s, ds) and self.str_judge(res, ds):
                res = ds

        return res

    def is_subsequence(self, s, ds):
        i, j = 0, 0
        length_s, length_ds = len(s), len(ds)

        while i < length_s and j < length_ds:
            if s[i] == ds[j]:
                j += 1
            i += 1

        return j == length_ds

    def str_judge(self, res, ds):
        if len(ds) > len(res):
            judge_flag = True
        elif len(ds) == len(res) and ds < res:
            judge_flag = True
        else:
            judge_flag = False

        return judge_flag
