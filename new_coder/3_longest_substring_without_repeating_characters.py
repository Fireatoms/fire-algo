# link: https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstringBrute(self, s: str) -> int:
        ans, length = 0, len(s)
        for i in range(length):
            max_length = 0
            cache = set()
            for j in range(i, length):
                if s[j] not in cache:
                    cache.add(s[j])
                    max_length += 1
                else:
                    break
            ans = max(max_length, ans)

        return ans

    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = set()
        length = len(s)
        rk, ans = 0, 0

        for i in range(length):
            if i > 0:
                # window left move
                cache.remove(s[i - 1])

            while rk < length and s[rk] not in cache:
                cache.add(s[rk])
                rk += 1

            ans = max(ans, rk - i)

        return ans


if __name__ == "__main__":
    sl = Solution()
    s = 'pwwkew'
    print(sl.lengthOfLongestSubstringBrute(s))