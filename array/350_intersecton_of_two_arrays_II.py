# link: https://leetcode.com/problems/intersection-of-two-arrays-ii/
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        short_nums = nums1
        long_nums = nums2
        if len(nums1) > len(nums2):
            short_nums = nums2
            long_nums = nums1

        short_counts = Counter(short_nums)
        for num in long_nums:
            if short_counts.get(num, 0) > 0:
                ans.append(num)
                short_counts[num] -= 1

        return ans