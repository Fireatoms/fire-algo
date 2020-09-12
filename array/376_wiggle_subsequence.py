# link: https://leetcode.com/problems/wiggle-subsequence/


class Solution:
    def wiggleMaxLengthDp(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return length
        down, up = [0] * length, [0] * length
        down[0], up[0] = 1, 1
        for i in range(1, length):
            if nums[i] - nums[i-1] > 0:
                up[i] = down[i-1] + 1
                down[i] = down[i-1]
            elif nums[i] - nums[i-1] < 0:
                down[i] = up[i-1] + 1
                up[i] = up[i-1]
            else:
                down[i] = down[i-1]
                up[i] = up[i-1]
        return max(up[-1], down[-1])

    def wiggleMaxLength(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return length

        down, up = 1, 1
        for i in range(1, length):
            if nums[i] - nums[i-1] > 0:
                up = down + 1
            elif nums[i] - nums[i-1] < 0:
                down = up + 1

        return max(down, up)

    def wiggleMaxLengthGreedy(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return length

        prediff = nums[1] - nums[0]
        count = 2 if prediff != 0 else 1
        for i in range(2, length):
            curdiff = nums[i] - nums[i-1]
            # prediff equal 0 only at the beginning.
            # prediff can not change to zero again once it has changed to a non-zero value
            if (curdiff < 0 and prediff >= 0) or (curdiff > 0 and prediff <= 0):
                count += 1
                prediff = curdiff

        return count