# link: https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first_eq = self.first_eq(nums, target)
        if first_eq == -1:
            return 0
        last_eq = self.last_eq(nums, target)
        return last_eq - first_eq + 1

    def first_eq(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                if mid <= 0 or nums[mid - 1] != target:
                    return mid
                else:
                    high = mid - 1
        return -1

    def last_eq(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                if mid >= len(nums) - 1 or nums[mid + 1] != target:
                    return mid
                else:
                    low = mid + 1
        return -1


if __name__ == "__main__":
    sl = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(sl.search(nums, 8))