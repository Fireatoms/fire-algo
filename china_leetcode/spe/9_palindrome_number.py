# link: https://leetcode-cn.com/problems/palindrome-number/


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverse = 0
        while x > reverse:
            reverse = 10 * reverse + x % 10
            x = x // 10

        return x == reverse or x == reverse // 10