# link: https://leetcode-cn.com/problems/single-number-ii/


class Solution:
    def singleNumberHashMap(self, nums: List[int]) -> int:
        hash_map = {}
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 0

            hash_map[num] = hash_map[num] +1

        for k, v in hash_map.items():
            if v == 1:
                return k

    def singleNumberHashSet(self, nums: List[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums)) // 2

    def singleNumber(self, nums: List[int]) -> int:
        x, y = 0, 0
        for num in nums:
            y = ~x & (y ^ num)
            x = ~y & (x ^ num)

        return y

    def singleNumberNative(self, nums: List[int]) -> int:
        x, y = 0, 0
        for num in nums:
            y_new = ~x & (y ^ num)
            x = (x & ~y & ~num) | (~x & y & num)
            y = y_new

        return y