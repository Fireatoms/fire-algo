# link: https://leetcode.com/problems/merge-sorted-array/
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp = [0] * (m+n)
        i, j, k = 0, 0, 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                tmp[k] = nums1[i]
                i += 1
            else:
                tmp[k] = nums2[j]
                j += 1
            k += 1

        if i < m:
            tmp[k:] = nums1[i:m]
        else:
            tmp[k:] = nums2[j:n]

        for i in range(len(tmp)):
            nums1[i] = tmp[i]

    def merge_space_saving(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, p = m-1, n-1, m+n-1
        while p1 >= 0 and p2 >= 0:
            if nums2[p2] >= nums1[p1]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        # wrong! Because when p2 = -1, we do not need to copy nums2 to nums1
        # nums1[:p+1] = nums2[:p2+1]
        nums1[:p2+1] = nums2[:p2+1]

if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    sl = Solution()
    sl.merge_space_saving(nums1, 3, nums2, 3)
    print(nums1)