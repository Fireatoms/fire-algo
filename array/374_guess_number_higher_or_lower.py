# link: https://leetcode.com/problems/guess-number-higher-or-lower/


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid = low + (high-low) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def binary_search(self, target, arr):
        low, high = 0, len(arr) - 1
        while low < high:
            mid = low + (high-low) // 2
            if arr[mid] >= target:
                high = mid
            else:
                low = mid + 1

        return low


if __name__ == "__main__":
    arr = [i for i in range(1, 10)]
    print(arr)
    sl = Solution()
    print(sl.binary_search(0, arr))