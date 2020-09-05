# link: https://leetcode.com/problems/majority-element-ii/


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        candidate1, candidate2, counter1, counter2 = None, None, 0, 0
        for n in nums:
            if n == candidate1:
                counter1 += 1
            elif n == candidate2:
                counter2 += 1
            elif counter1 == 0:
                candidate1 = n
                counter1 += 1
            elif counter2 == 0:
                candidate2 = n
                counter2 += 1
            else:
                counter1 -= 1
                counter2 -= 1

        return [c for c in [candidate1, candidate2] if nums.count(c) > len(nums) // 3]