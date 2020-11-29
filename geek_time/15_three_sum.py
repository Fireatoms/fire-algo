# link: https://leetcode-cn.com/problems/3sum/
from typing import List


class Solution:
    def threeSumSet(self, nums: List[int]) -> List[List[int]]:
        res = set()
        length = len(nums)
        nums.sort()
        for i in range(length-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            cache = set()
            for j in range(i+1, length):
                if -nums[i] - nums[j] in cache:
                    if (nums[i], -nums[i]-nums[j], nums[j]) in res:
                        print((nums[i], -nums[i]-nums[j], nums[j]))
                    res.add((nums[i], -nums[i]-nums[j], nums[j]))
                cache.add(nums[j])
        return list(map(list, res))

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)
        nums.sort()
        for i in range(length-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i + 1, length - 1
            while j < k:
                if nums[j] + nums[k] > -nums[i]:
                    k -= 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
        return res

    def threeSumBrute(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)
        nums.sort()
        for i in range(length-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, length-1):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                for k in range(j+1, length):
                    if k > j+1 and nums[k] == nums[k-1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.append([nums[i], nums[j], nums[k]])
        return res


if __name__ == "__main__":
    nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
    nums.sort()
    print(nums)
    sl = Solution()
    # sl.threeSumSet(nums)

    # nums = [-1, 0, 1, 2, -1, -4]
    # sl = Solution()
    res = sl.threeSumBrute(nums)
    print(res)
    # # res = sl.threeSumSet(nums)
    # res = sl.threeSum(nums)
    # print(res)