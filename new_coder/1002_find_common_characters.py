# link: https://leetcode-cn.com/problems/find-common-characters/
from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        char_freq = [128] * 26

        for s in A:
            cur_freq = [0] * 26
            for c in s:
                cur_freq[ord(c) - ord('a')] += 1
            for i in range(26):
                char_freq[i] = min(char_freq[i], cur_freq[i])

        ans = []
        for i in range(26):
            ans.extend([chr(ord('a') + i)] * char_freq[i])
        return ans

    def commonCharsHash(self, A: List[str]) -> List[str]:
        if not A:
            return []

        init_dict = {}
        for s in A[0]:
            init_dict[s] = init_dict.get(s, 0) + 1

        for s in A[1:]:
            cur_dict = {}
            for c in s:
                cur_dict[c] = cur_dict.get(c, 0) + 1

            for k in init_dict:
                if k in cur_dict:
                    init_dict[k] = min(init_dict[k], cur_dict[k])
                else:
                    init_dict[k] = 0

        ans = []
        # for k, v in init_dict.items():
        #     ans.extend([k] * v)

        for k, v in init_dict.items():
            for i in range(v):
                ans.append(k)

        return ans


if __name__ == "__main__":
    a = ["bella","label","roller"]
    sl = Solution()
    print(sl.commonChars(a))
    print(sl.commonCharsHash(a))