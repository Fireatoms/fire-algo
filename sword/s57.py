# link: https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        j, k = 0, len(nums) - 1
        while j < k:
            if nums[j] + nums[k] == target:
                ans.append(nums[j])
                ans.append(nums[k])
                break
            elif nums[j] + nums[k] > target:
                k -= 1
            else:
                j += 1
        return ans


if __name__ == "__main__":
    sl = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(sl.twoSum(nums, target))