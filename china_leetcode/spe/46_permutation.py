# link: https://leetcode-cn.com/problems/permutations/
import copy


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)
        if length == 0:
            return res

        path = []
        used = [False] * length
        self.dfs(nums, length, 0, path, used, res)
        return res

    def dfs(self, nums, length, depth, path, used, res):
        if depth == length:
            res.append(copy.deepcopy(path))
            return

        for i in range(length):
            if used[i]:
                continue

            path.append(nums[i])
            used[i] = True
            self.dfs(nums, length, depth + 1, path, used, res)
            path.pop()
            used[i] = False

    # difficult for understanding
    def permute_imrpove(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)
        self.backtrack(nums, length, 0, res)
        return res

    def backtrack(self, nums, length, depth, res):
        if depth == length:
            res.append(copy.deepcopy(nums))
            return

        for i in range(depth, length):
            nums[depth], nums[i] = nums[i], nums[depth]
            self.backtrack(nums, length, depth + 1, res)
            nums[depth], nums[i] = nums[i], nums[depth]

