# link: https://leetcode.com/problems/first-unique-character-in-a-string/


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for str in s:
            count[str] = count.get(str, 0) + 1

        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx

        return -1