# link: https://leetcode.com/problems/maximum-product-subarray/
from typing import List


class Solution:
    # wrong
    def maxProductWrong(self, nums: List[int]) -> int:
       ans = float('-inf')
       length = len(nums)
       for i in range(length):
           cur_max = nums[i]
           for j in range(i+1, length):
               # no consideration of negative numbers
               if cur_max * nums[j] < cur_max:
                   break
               cur_max *= nums[j]
           ans = max(ans, cur_max)

       return ans

    def maxProductBrute(self, nums: List[int]) -> int:
        ans = float('-inf')
        length = len(nums)
        for i in range(length):
            pro_list = [float('-inf')] * (length - i)
            pro_list[0] = nums[i]
            for j in range(i+1, length):
                pro_list[j-i] = pro_list[j-i-1] * nums[j]
            ans = max(ans, max(pro_list))

        return ans

    def maxProductDp(self, nums: List[int]) -> int:
        length = len(nums)
        max_state, min_state = [0] * length, [0] * length
        max_state[0], min_state[0] = nums[0], nums[0]
        for i in range(1, length):
            max_state[i] = max(max_state[i-1]*nums[i], min_state[i-1]*nums[i], nums[i])
            min_state[i] = min(min_state[i-1]*nums[i], max_state[i-1]*nums[i], nums[i])

        print(max_state)
        print(min_state)
        return max(max_state)

    def maxProduct(self, nums: List[int]) -> int:
        length = len(nums)
        min_pro, max_pro, ans = nums[0], nums[0], nums[0]
        for i in range(1, length):
            cur_min, cur_max = min_pro, max_pro
            min_pro = min(cur_min*nums[i], cur_max*nums[i], nums[i])
            max_pro = max(cur_min*nums[i], cur_max*nums[i], nums[i])
            ans = max(ans, max_pro)
        return ans

if __name__ == "__main__":
    arr = [-2, 3, -4]
    sl = Solution()
    print(sl.maxProductDp(arr))