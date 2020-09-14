# link: https://leetcode.com/problems/find-peak-element/


class Solution:
    # i like this. this reflects a certain code design ability.haha
    # but it is not good enough, because it does not making good use of existing conditions
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        for i in range(len(nums)):
            if self.is_peak(nums, i):
                return i

    def is_peak(self, nums, i):
        if i == 0 and nums[i+1] < nums[i]:
            return True

        if i == len(nums) - 1 and nums[i] > nums[i-1]:
            return True

        if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
            return True

        return False

    def findPeakElementBetter(self, nums: List[int]) -> int:
        for i in range(0, len(nums)-1):
            if nums[i] > nums[i+1]:
                return i
        # if nums is monotonically increasing, the last position must be the peak
        return len(nums) - 1

    def findPeakElementBinarySearch(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high-low) // 2
            if nums[mid] > nums[mid+1]:
                high = mid
            else:
                low = mid + 1

        return low
