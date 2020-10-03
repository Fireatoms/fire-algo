class Solution:
    def find_the_first_large_equal_val(self, nums, target):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] >= target:
                if mid - 1 < 0 or nums[mid - 1] < target:
                    return mid
                else:
                    high = mid - 1
            else:
                low = mid + 1

        return -1

    def find_the_last_little_equal_val(self, nums, target):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] <= target:
                if mid + 1 > len(nums) - 1 or nums[mid + 1] > target:
                    return mid
                else:
                    low = mid + 1
            else:
                high = mid - 1

        return -1


if __name__ == "__main__":
    sl = Solution()
    arr = [1, 2, 3, 3, 4, 4, 5]
    print(sl.find_the_first_large_equal_val(arr, 3))
    print(sl.find_the_last_little_equal_val(arr, 4))