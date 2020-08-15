# link: https://leetcode.com/problems/next-greater-element-i/
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res_list = []
        if not nums1:
            return []
        if not nums2:
            return [-1] * len(nums1)
        for k1, n1 in enumerate(nums1):
            res = -1
            if n1 not in nums2:
                res_list.append(res)
                continue
            idx = nums2.index(n1)
            for i in range(idx + 1, len(nums2)):
                if nums2[i] > n1:
                    res = nums2[i]
                    break
            res_list.append(res)

        return res_list


class Solution1:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater_dict = {}
        stack = []
        res = []

        for n in nums2:
            while stack and stack[-1] < n:
                greater_dict[stack.pop()] = n
            stack.append(n)

        for v in nums1:
            res.append(greater_dict.get(v, -1))

        return res
