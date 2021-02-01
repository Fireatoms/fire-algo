# link: https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] <= mid:
                low = mid + 1
            else:
                if mid <= 0 or nums[mid - 1] <= mid - 1:
                    return mid
                else:
                    high = mid - 1
        return len(nums)


if __name__ == "__main__":
    sl = Solution()
    # nums = [0,1,3]
    nums = [0,1,2,3,4,5,6,7,9]
    print(sl.missingNumber(nums))