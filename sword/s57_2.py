# link: https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i, j, cur_sum, ans = 1, 2, 3, []
        while i < j:
            if cur_sum == target:
                ans.append(list(range(i, j+1)))
                cur_sum -= i
                i += 1
            elif cur_sum > target:
                cur_sum -= i
                i += 1
            else:
                j += 1
                cur_sum += j
        return ans

    def findContinuousSequenceOrigin(self, target: int) -> List[List[int]]:
        ans = []
        cur_list = []
        cur_sum = 0
        for i in range(1, target // 2 + 2):
            cur_list.append(i)
            cur_sum += i
            if cur_sum == target and len(cur_list) > 1:
                ans.append(cur_list[:])
            while cur_sum > target:
                cur_sum -= cur_list[0]
                cur_list = cur_list[1:]
                if cur_sum == target and len(cur_list) > 1:
                    ans.append(cur_list[:])

        return ans


if __name__ == "__main__":
    sl = Solution()
    target = 15
    print(sl.findContinuousSequence(target))