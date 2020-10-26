# link: https://leetcode-cn.com/problems/majority-element/
from typing import List


class Solution:
    def majorityElementHash(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        majority = ''
        for i, v in count.items():
            if not majority:
                majority = i
                continue
            if v > count[majority]:
                majority = i

        return majority

        # return max(count.keys(), key=count.get)

    def majorityElementDevide(self, nums: List[int]) -> int:
        return self.majority_recur(nums, 0, len(nums) - 1)

    def majority_recur(self, nums, low, high):
        if low == high:
            return nums[low]

        mid = low + (high - low) // 2
        left_majority = self.majority_recur(nums, low, mid)
        right_majority = self.majority_recur(nums, mid+1, high)

        if left_majority == right_majority:
            return left_majority

        left_majority_count = sum(1 for i in nums[low:mid+1] if i == left_majority)
        right_majority_count = sum(1 for i in nums[mid+1:high+1] if i == right_majority)
        return left_majority if left_majority_count > right_majority_count else right_majority

    def majorityElementBm(self, nums: List[int]) -> int:
        candidate = ''
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate


if __name__ == "__main__":
    # nums = [1, 2, 1, 1, 2, 2, 1, 3, 1, 1, 1, 1]
    nums = [1, 1, 2, 2, 2, 2, 1, 1, 1, 3, 3]
    sl = Solution()
    print(sl.majorityElementDevide(nums))