# link: https://leetcode.com/problems/reverse-vowels-of-a-string/


class Solution:
    def reverseVowels(self, s: str) -> str:
        sa = [sv for sv in s]
        left, right = 0, len(s) - 1
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        while left < right:
            while left < right and sa[left] not in vowels:
                left += 1
            while left < right and sa[right] not in vowels:
                right -= 1

            sa[left], sa[right] = sa[right], sa[left]
            left += 1
            right -= 1

        return ''.join(sa)
