# link: https://leetcode.com/problems/summary-ranges/


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i, j = 0, 0
        length = len(nums)
        ans = []
        while j < length:
            if j + 1 < length and nums[j+1] - nums[j] == 1:
                j += 1
            else:
                if j == i:
                    ans.append(str(nums[i]))
                else:
                    ans.append(str(nums[i]) + '->' + str(nums[j]))
                j += 1
                i = j

        return ans