# link: https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if candidate == num:
                count += 1
            else:
                count -= 1
        return candidate

    def majorityElementHash(self, nums: List[int]) -> int:
        count_dict = {}
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
        return max(count_dict.keys(), key=count_dict.get)


if __name__ == "__main__":
    sl = Solution()
    nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    print(sl.majorityElement(nums))