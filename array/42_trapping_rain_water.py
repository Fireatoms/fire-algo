# link: https://leetcode.com/problems/trapping-rain-water/


class Solution:
    def trap_brute(self, height: List[int]) -> int:
        ans = 0
        for i in range(len(height)):
            left_max, right_max = 0, 0
            for j in range(i, -1, -1):
                left_max = max(left_max, height[j])
            for k in range(i, len(height)):
                right_max = max(right_max, height[k])

            ans += min(left_max, right_max) - height[i]

        return ans

    def trap_dp(self, height: List[int]) -> int:
        if not height:
            return 0

        ans, size = 0, len(height)
        left_max = [0] * size
        right_max = [0] * size
        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i-1], height[i])

        right_max[size-1] = height[size-1]
        for i in range(size-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])

        for i in range(size):
            ans += min(left_max[i], right_max[i]) - height[i]

        return ans