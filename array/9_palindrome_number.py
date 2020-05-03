# link: https://leetcode.com/problems/palindrome-number/


class Solution:
    """转成字符串
    目的：练习双指针的一般解法
    """
    def isPalindrome(self, x):
        sx = str(x)
        sa = []
        for v in sx:
            sa.append(v)
        i = 0
        j = len(sa) - 1
        while i < j:
            if sa[i] == sa[j]:
                i += 1
                j -= 1
            else:
                break

        return i >= j

    def isPalindromeInt(self, x):
        """
        在/上踩坑
        :param x:
        :return:
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverse_num = 0
        while reverse_num < x:
            reverse_num = reverse_num * 10 + x % 10
            x //= 10

        return reverse_num == x or reverse_num // 10 == x


def test_p():
    pc = Solution()
    print(pc.isPalindromeInt(11))

if __name__ == "__main__":
    test_p()