# link: https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, s_len = 0, len(s)
        appeared_set = set()
        right = 0
        for left in range(s_len):
            if left > 0: appeared_set.remove(s[left - 1])
            while right < s_len and s[right] not in appeared_set:
                appeared_set.add(s[right])
                right += 1
            ans = max(ans, right - left)
        return ans


if __name__ == "__main__":
    sl = Solution()
    print(sl.lengthOfLongestSubstring("abcabcbb"))