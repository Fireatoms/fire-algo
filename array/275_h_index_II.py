# link: https://leetcode.com/problems/h-index-ii/


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = len(citations)
        for k, v in enumerate(citations):
            if v >= l - k:
                return l - k

        return 0

    def hIndexBinary(self, citations: List[int]) -> int:
        l = len(citations)
        low, high = 0, l - 1
        while low <= high:
            mid = low + (high - low) // 2
            if citations[mid] == l - mid:
                return l - mid
            elif citations[mid] > l - mid:
                high = mid - 1
            else:
                low = mid + 1

        return l - low