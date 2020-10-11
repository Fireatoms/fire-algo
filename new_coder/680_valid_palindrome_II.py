# link: https://leetcode-cn.com/problems/valid-palindrome-ii/


class Solution:
    def validPalindrome(self, s: str) -> bool:
        low, high = 0, len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return self.check_palindrome(s, low + 1, high) or self.check_palindrome(s, low, high - 1)

        return True

    def check_palindrome(self, s, low, high):
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return False

        return True
