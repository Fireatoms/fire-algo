# link: https://leetcode-cn.com/problems/minimum-window-substring/


class Solution:
    def check(self, target_dict, current_dict):
        for tk in target_dict:
            if tk not in current_dict or current_dict[tk] < target_dict[tk]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        s_len = len(s)
        left, right, ans_left, ans_right = 0, 0, -1, -1
        target_dict, current_dict = {}, {}
        min_len = float("inf")
        for st in t:
            target_dict[st] = target_dict.get(st, 0) + 1
        while left < s_len and right < s_len:
            if s[right] in target_dict:
                current_dict[s[right]] = current_dict.get(s[right], 0) + 1
            while left <= right and self.check(target_dict, current_dict):
                if right - left + 1 < min_len:
                    ans_left, ans_right = left, right
                    min_len = right - left + 1
                if s[left] in current_dict:
                    current_dict[s[left]] -= 1
                left += 1
            right += 1
        return s[ans_left:ans_right+1] if ans_left != -1 else ""


if __name__ == "__main__":
    sl = Solution()
    s = "DBANCD"
    t = "ABC"
    print(sl.minWindow(s, t))
