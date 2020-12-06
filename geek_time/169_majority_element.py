# link: https://leetcode-cn.com/problems/majority-element/
from typing import List


class Solution:
    def majorityElementBm(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for n in nums:
            if count == 0:
                candidate = n
            if candidate == n:
                count += 1
            else:
                count -= 1
        return candidate

    def majorityElementDivide(self, nums: List[int]) -> int:
        return self.majority_element_recur(nums, 0, len(nums)-1)

    def majority_element_recur(self, nums, low, high):
        if low == high:
            return nums[low]
        mid = low + (high - low) // 2
        left = self.majority_element_recur(nums, low, mid)
        right = self.majority_element_recur(nums, mid+1, high)
        if left == right:
            return left
        left_count = sum(1 for i in range(low, high+1) if nums[i] == left)
        right_count = sum(1 for i in range(low, high+1) if nums[i] == right)
        return left if left_count > right_count else right

    def majorityElement(self, nums: List[int]) -> int:
        num_map = {}
        for n in nums:
            num_map[n] = num_map.get(n, 0) + 1
        return max(num_map.keys(), key=num_map.get)


if __name__ == "__main__":
    nums = [3, 3, 4]
    sl = Solution()
    print(sl.majorityElement(nums))
    print(sl.majorityElementDivide(nums))
    print(sl.majorityElementBm(nums))

