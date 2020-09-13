# link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# reference: https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/solution/er-fen-cha-zhao-wei-shi-yao-zuo-you-bu-dui-cheng-z/
# amazing
from typing import List


class Solution:
    # not a good solution
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        low, high = 0, len(nums) - 1
        if nums[high] > nums[low]:
            return nums[low]

        while low <= high:
            mid = low + (high-low) // 2
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]

            if nums[0] < nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

    def findMinSimplifyLeft(self, nums: List[int]) -> int:
        #  wrong, judging on low does not work
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high-low) // 2 + 1
            if nums[low] < nums[mid]:
                low = mid
            else:
                high = mid - 1

        return nums[(low+1)%len(nums)]

    def findMinSimplifyRight(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high-low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]



if __name__ == "__main__":
    arr = [1, 2]
    sl = Solution()
    sl.findMinSimplifyLeft(arr)
