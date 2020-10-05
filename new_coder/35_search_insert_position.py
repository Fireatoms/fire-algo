class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] >= target:
                high = mid
            else:
                low = mid + 1

        return low if nums[low] >= target else low + 1

    def searchInsertEasy(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] >= target:
                if mid - 1 < 0 or nums[mid - 1] < target:
                    return mid
                else:
                    high = mid -1
            else:
                low = mid + 1

        return len(nums)