#link: https://leetcode.com/problems/sqrtx/


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1

        low, high = 0, x
        root = 0
        while low <= high:
            mid = (high - low) // 2 + low
            if mid == x / mid:
                root = mid
                break
            elif mid > x / mid:
                # high -= 1
                high = mid - 1
            else:
                root = mid
                # fuck binary search!
                # low += 1
                low = mid + 1

        return int(root)


if __name__ == "__main__":
    sl = Solution()
    print(sl.mySqrt(5))