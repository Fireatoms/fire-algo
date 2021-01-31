# link: https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s = list(s)
        self.reverse(s, 0, n - 1)
        self.reverse(s, n, len(s) - 1)
        self.reverse(s, 0, len(s) - 1)
        return ''.join(s)

    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1


if __name__ == "__main__":
    sl = Solution()
    s = "abcdefg"
    print(sl.reverseLeftWords(s, 2))