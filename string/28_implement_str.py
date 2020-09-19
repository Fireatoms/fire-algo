# link: https://leetcode.com/problems/implement-strstr/


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            j = 0
            while j < m:
                if haystack[i + j] != needle[j]:
                    break
                j += 1

            if j == m:
                return i

        return -1

    def strStrRk(self, haystack: str, needle: str) -> int:
        # Time Limit Exceeded,
        base = 26
        n, m = len(haystack), len(needle)
        if n < m:
            return -1
        # hay_hash = [0] * (n - m + 1)
        hay_hash_begin = 0
        needle_hash = 0
        for i in range(m):
            hay_hash_begin += pow(base, m - i - 1) * (ord(haystack[i]) - ord('a'))
            needle_hash += pow(base, m - i - 1) * (ord(needle[i]) - ord('a'))

        if hay_hash_begin == needle_hash:
            return 0

        # hay_hash[0] = hay_hash_begin
        # for i in range(1, n - m + 1):
        #     hay_hash[i] = base * (hay_hash[i - 1] - pow(base, m - 1) * (ord(haystack[i - 1]) - ord('a'))) + ord(haystack[i + m - 1]) - ord('a')

        hay_hash_value = hay_hash_begin
        base_m = pow(base, m - 1)
        for i in range(1, n - m + 1):
            hay_hash_value = base * (hay_hash_value - base_m * (ord(haystack[i - 1]) - ord('a'))) + ord(haystack[i + m - 1]) - ord('a')
            if hay_hash_value == needle_hash:
                return i

        return -1


if __name__ == "__main__":
    haystack = 'hello'
    needle = 'll'
    sl = Solution()
    print(sl.strStrRk(haystack, needle))