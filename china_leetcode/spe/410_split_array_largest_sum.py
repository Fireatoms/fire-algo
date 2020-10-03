# link: https://leetcode-cn.com/problems/split-array-largest-sum/


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        low, high = max(nums), sum(nums)

        while low < high:
            mid = low + (high - low) // 2
            if self.check(nums, mid, m):
                high = mid
            else:
                low = mid + 1
        return low

    def check(self, nums, x, m):
        total, cnt = 0, 1
        for num in nums:
            if total + num > x:
                cnt += 1
                total = num
            else:
                total += num

        return cnt <=  m