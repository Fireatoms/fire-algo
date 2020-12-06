# link: https://leetcode-cn.com/problems/3sum/
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        res = []
        for i in range(length-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i + 1, length - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
        return res

    def threeSumSet(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        res = set()
        for i in range(length-2):
            # It is unnecessary, but this help significantly reduce the execution time of the program
            if i > 0 and nums[i] == nums[i-1]:
                continue
            cached = set()
            for j in range(i+1, length):
                if -nums[i] - nums[j] in cached:
                    res.add((nums[i], -nums[i]-nums[j], nums[j]))
                else:
                    cached.add(nums[j])

        return list(map(list, res))


if __name__ == "__main__":
    nums = [-4, -4, -2, -2, -1, 1, 2, 2, 3 ,4]
    sl = Solution()
    print(sl.threeSum(nums))