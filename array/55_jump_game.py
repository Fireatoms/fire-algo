# link: https://leetcode.com/problems/jump-game/


class Solution:
    def canJumpGeedy(self, nums: List[int]) -> bool:
        if not nums:
            return False

        farthest, i = 0, 0
        while i <= farthest and i < len(nums):
            farthest = max(farthest, i+nums[i])
            i += 1

        if farthest >= len(nums) - 1:
            return True

        return False

    def canJumpBackTracking(self, nums: List[int]) -> bool:
        return self.can_jump_r(0, nums)

    def can_jump_r(self, position, nums):
        if position == len(nums) - 1:
            return True

        furthest_jump = min(position + nums[position], len(nums) - 1)
        # for i in range(position + 1, furthest_jump + 1):
        for i in range(furthest_jump, position, -1):
            if self.can_jump_r(i, nums):
                return True

        return False

    def canJumpBackTrackingMemo(self, nums: List[int]) -> bool:
        # 0: unknown 1: good 2: bad
        self.memo = [0] * len(nums)
        self.memo[len(nums)-1] = 1
        return self.can_jump_mr(0, nums)

    def can_jump_mr(self, position, nums):
        if self.memo[position] == 1:
            return True

        if self.memo[position] == 2:
            return False

        furthest_jump = min(position + nums[position], len(nums) - 1)
        for i in range(furthest_jump, position, -1):
            if self.can_jump_mr(i, nums):
                self.memo[position] = 1
                return True

        self.memo[position] = False

    def canJumpGeedy1(self, nums: List[int]) -> bool:
        last_pos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= last_pos:
                last_pos = i

        return last_pos == 0


