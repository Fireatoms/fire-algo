# link: https://leetcode-cn.com/problems/sqrtx/


class Solution:
    def mySqrt(self, x: int) -> int:
        low, high, ans = 0, x, -1
        while low <= high:
            mid = low + (high - low) // 2
            if mid * mid <= x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans


if __name__ == "__main__":
    sl = Solution()
    print(sl.mySqrt(101))