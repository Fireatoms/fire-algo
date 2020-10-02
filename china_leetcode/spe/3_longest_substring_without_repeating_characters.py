# link: https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstringBrute(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0

        ans = 1
        for i in range(length):
            max_length = 0
            cache = set()
            for j in range(i, length):
                if s[j] not in cache:
                    max_length += 1
                    cache.add(s[j])
                else:
                    break
            ans = max(ans, max_length)

        return ans

    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0

        cache = {}
        max_length = 0
        current_length = 0
        start_index = 0

        for i in range(length):
            if s[i] not in cache:
                current_length += 1
                cache[s[i]] = i
            else:
                max_length = max(max_length, current_length)
                start_index = max(start_index, cache[s[i]])
                cache[s[i]] = i
                current_length = i - start_index

        max_length = max(max_length, current_length)

        return max_length


if __name__ == "__main__":
    s = 'pwwkew'
    sl = Solution()
    print(sl.lengthOfLongestSubstringBrute(s))