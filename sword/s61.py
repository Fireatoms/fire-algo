# link: https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/
from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        max_val, min_val = 0, 14
        visited = set()
        for num in nums:
            if num == 0:
                continue
            if num in visited:
                return False
            visited.add(num)
            if num > max_val:
                max_val = num
            if num < min_val:
                min_val = num
        return max_val - min_val < 5


if __name__ == "__main__":
    sl = Solution()
    print(sl.isStraight([0, 0, 1, 2, 5]))