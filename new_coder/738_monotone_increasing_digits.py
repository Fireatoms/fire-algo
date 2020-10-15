# link: https://leetcode-cn.com/problems/monotone-increasing-digits/


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        n_list = list(map(int,str(N)))
        n_length = len(n_list)
        i = 1
        while i < n_length and n_list[i - 1] <= n_list[i]:
            i += 1
        while 0 < i < n_length and n_list[i - 1] > n_list[i]:
            n_list[i - 1] -= 1
            i -= 1
        n_list[i+1:] = [9] * (n_length - 1 - i)
        return int(''.join(map(str, n_list)))


if __name__ == "__main__":
    n = 132
    sl = Solution()
    print(sl.monotoneIncreasingDigits(n))