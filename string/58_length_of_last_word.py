# link: https://leetcode.com/problems/length-of-last-word/


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        start, end = -1, -1

        for i in range(len(s) - 1, -1, -1):
            if start != -1 and end != -1:
                break
            if start == -1:
                if s[i] != ' ':
                    start = i
            else:
                if s[i] == ' ':
                    end = i

        if start != -1:
            return start - end

        return 0