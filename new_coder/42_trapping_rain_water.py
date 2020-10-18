# link: https://leetcode-cn.com/problems/trapping-rain-water/
from typing import List


class Solution:
    def trapBrute(self, height: List[int]) -> int:
        ans, length = 0, len(height)
        for i in range(length):
            max_left, max_right = 0, 0
            for j in range(i, -1, -1):
                max_left = max(max_left, height[j])
            for j in range(i, length):
                max_right = max(max_right, height[j])

            ans += min(max_left, max_right) - height[i]

        return ans

    def trap_dp(self, height: List[int]) -> int:
        if not height:
            return 0

        ans, length = 0, len(height)
        left_max = [0] * length
        right_max = [0] * length
        left_max[0] = height[0]
        right_max[-1] = height[-1]

        for i in range(1, length):
            left_max[i] = max(left_max[i-1], height[i])
        for i in range(length - 2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])

        for i in range(length):
            ans += min(left_max[i], right_max[i]) - height[i]

        return ans

    def trap_pointer(self, height: List[int]) -> int:
        ans, length = 0, len(height)
        left, right = 0, length - 1
        left_max, right_max = 0, 0

        while left < right:
            if height[left] < height[right]:
                if left_max <= height[left]:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if right_max <= height[right]:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1

        return ans


if __name__ == "__main__":
    arr = [0,1,0,2,1,0,1,3,2,1,2,1]
    sl = Solution()
    print(sl.trapBrute(arr))
    print(sl.trap_dp(arr))
    print(sl.trap_pointer(arr))