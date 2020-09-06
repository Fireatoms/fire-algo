# link: https://leetcode.com/problems/contains-duplicate-ii/


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        record = {}
        for i, v in enumerate(nums):
            if v in record:
                if i - record[v] <= k:
                    return True
            record[v] = i