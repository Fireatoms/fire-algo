# link: https://leetcode.com/problems/reverse-words-in-a-string/
from collections import deque


class Solution:
    def reverseWordsOneLine(self, s: str) -> str:
        return ''.join(reversed(s.split()))

    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s) - 1
        while left <= right and s[left] == ' ':
            left += 1

        while left <= right and s[right] == ' ':
            right -= 1

        que, word = deque(), ''
        while left <= right:
            if s[left] == ' ' and word:
                que.appendleft(word)
                word = ''
            elif s[left] != ' ':
                word += s[left]
            left += 1

        if word:
            que.appendleft(word)

        return ' '.join(que)
