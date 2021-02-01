# link: https://leetcode-cn.com/problemset/lcof/?difficulty=%E7%AE%80%E5%8D%95


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        i = j = len(s) - 1
        ans = []
        while i >= 0:
            while i >= 0 and s[i] != " ":
                i -= 1
            ans.append(s[i+1:j+1])
            while i >= 0 and s[i] == " ":
                i -= 1
            j = i
        return " ".join(ans)


if __name__ == "__main__":
    s = "  hello world!  "
    sl = Solution()
    print(sl.reverseWords(s))