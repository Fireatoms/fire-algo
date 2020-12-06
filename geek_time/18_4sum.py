# link: https://leetcode-cn.com/problems/4sum/
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        res = []
        for i in range(length-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[length-3] + nums[length-2] + nums[length-1] < target:
                continue
            for j in range(i+1, length-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[length-2] + nums[length-1] < target:
                    continue
                k, m = j + 1, length - 1
                while k < m:
                    if nums[i] + nums[j] + nums[k] + nums[m] < target:
                        k += 1
                    elif nums[i] + nums[j] + nums[k] + nums[m] > target:
                        m -= 1
                    else:
                        res.append([nums[i], nums[j], nums[k], nums[m]])
                        while k < m and nums[k] == nums[k+1]:
                            k += 1
                        while k < m and nums[m] == nums[m-1]:
                            m -= 1
                        k += 1
                        m -= 1
        return res

    def fourSumLow(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        res = []
        for i in range(length-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, length-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                k, m = j + 1, length - 1
                while k < m:
                    if nums[i] + nums[j] + nums[k] + nums[m] < target:
                        k += 1
                    elif nums[i] + nums[j] + nums[k] + nums[m] > target:
                        m -= 1
                    else:
                        res.append([nums[i], nums[j], nums[k], nums[m]])
                        while k < m and nums[k] == nums[k+1]:
                            k += 1
                        while k < m and nums[m] == nums[m-1]:
                            m -= 1
                        k += 1
                        m -= 1
        return res


if __name__ == "__main__":
    nums = [-4, -4, -2, -2, -1, 1, 2, 2, 3, 4]
    sl = Solution()
    print(sl.fourSum(nums, -2))