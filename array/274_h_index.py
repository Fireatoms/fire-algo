# link: https://leetcode.com/problems/h-index/


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        i = 0
        l = len(citations)
        while i < l and citations[l-i-1] > i:
            i += 1

        return i

    def hIndexCount(self, citations: List[int]) -> int:
        l = len(citations)
        citations_count = [0] * (l+1)

        for c in citations:
            citations_count[min(c, l)] += 1

        k = l
        s = citations_count[k]
        while k > s:
            k -= 1
            s += citations_count[k]

        return k


