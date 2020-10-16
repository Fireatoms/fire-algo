# link: https://leetcode-cn.com/problems/reverse-words-in-a-string/
from collections import deque


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))

    def reverseWordsSelf(self, s: str)-> str:
        if not s:
            return ''
        # trim
        length = len(s)
        i, j = 0, length - 1

        while i < length and s[i] == ' ':
            i += 1

        while j >= 0 and s[j] == ' ':
            j -= 1

        queue, word = deque(), []

        for k in range(i, j + 1):
            if s[k] == ' ' and word:
                queue.appendleft(''.join(word))
                word = []
            elif s[k] != ' ':
                word.append(s[k])

        if word:
            queue.appendleft(''.join(word))

        return ' '.join(queue)


if __name__ == "__main__":
    s = ' this is my house '
    sl = Solution()
    print(sl.reverseWordsSelf(s))