# link: https://leetcode.com/problems/contains-duplicate-iii/


class Solution:
    # brute force: time limit exceeded
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        l = len(nums)
        for i in range(l):
            for j in range(i+1, min(i+k+1, l)):
                if abs(nums[j] - nums[i]) <= t:
                    return True

        return False