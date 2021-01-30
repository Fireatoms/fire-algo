# link: https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans += n & 1
            n >>= 1
        return ans

    def hammingWeightPerfect(self, n: int) -> int:
        ans = 0
        while n:
            ans += 1
            n &= n - 1
        return ans


if __name__ == "__main__":
    sl = Solution()
    print(sl.hammingWeightPerfect(8))