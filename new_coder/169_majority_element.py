# link: https://leetcode-cn.com/problems/majority-element/


class Solution:
    def majorityElementHash(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        majority = ''
        for i, v in count.items():
            if not majority:
                majority = i
                continue
            if v > count[majority]:
                majority = i

        return majority

        # return max(count.keys(), key=count.get)