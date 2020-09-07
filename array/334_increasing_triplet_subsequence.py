# link: https://leetcode.com/problems/increasing-triplet-subsequence/


class Solution:
    # 4252ms unbelievable, it can pass.
    def increasingTripletBrute(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    for k in range(j+1, len(nums)):
                        if nums[k] > nums[j]:
                            return True

        return False

    def increasingTriplet(self, nums: List[int]) -> bool:
        r1, r2 = float('inf'), float('inf')
        for i in range(len(nums)):
            if nums[i] <= r1:
                r1 = nums[i]
            elif nums[i] <= r2:
                r2 = nums[i]
            else:
                return True

        return False