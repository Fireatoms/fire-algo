# link: https://leetcode-cn.com/problems/single-number-iii/


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hash_map = {}
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 0
            hash_map[num] += 1

        return [i for i in hash_map if hash_map[i] == 1]

    def singleNumberXor(self, nums: List[int]) -> List[int]:
        bitmask = 0
        for num in nums:
            bitmask ^= num

        diff = bitmask & (~bitmask + 1)

        x = 0
        for num in nums:
            if num & diff:
                x ^= num

        return [x, bitmask ^ x]