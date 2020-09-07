# link: https://leetcode.com/problems/container-with-most-water/


class Solution:
    def maxAreaBrute(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)-1):
            for j in range(i+1, len(height)):
                cur = (j -i) * min(height[i], height[j])
                if cur > res:
                    res = cur

        return res

    def maxArea(self, height: List[int]) -> int:
        max_area, i, j = 0, 0, len(height) - 1
        while i < j:
            max_area = max(min(height[i], height[j])*(j-i), max_area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area