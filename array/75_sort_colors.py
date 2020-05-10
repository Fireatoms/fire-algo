# link: https://leetcode.com/problems/sort-colors/\


class Solution:
    """计数排序，比较死板的使用方式，通用的一个排序方式
    实际这题的求解可以简化：
    1. 明确了只有0，1，2三个数字
    2. 只需要统计0，1，2三个数字的个数即可
    """
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ac = [0] * 3
        for v in nums:
            ac[v] += 1

        for i in range(1, len(ac)):
            ac[i] = ac[i-1] + ac[i]

        tmp = [None] * len(nums)
        for v in reversed(nums):
            tmp[ac[v] - 1] = v
            ac[v] -= 1

        nums[:] = tmp


class Solution1:
    """根据题目具体情况简化的计数排序算法实现"""
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # record color num
        count_red = count_white = count_blue = 0
        for v in nums:
            if v == 0:
                count_red += 1
            elif v == 1:
                count_white += 1
            else:
                count_blue += 1

        nums[:count_red] = [0] * count_red
        nums[count_red: count_red + count_white] = [1] * count_white
        nums[count_red + count_white:] = [2] * count_blue


class Solution2:
    """维护三个指针，主旨思想是不断的将0往前移，2不断的往后移，每一个数字处理完毕后1自然在中间。注意我说的每一个数字处理完，所以
    循环条件上一定要有=，这样才能保证每一个数字得到处理
    从后往前的这个指针操作很像27题的remove_element
    """
    def sortColors(self, nums: List[int]) -> None:
        i, j, k = 0, 0, len(nums) - 1
        while i <= k:
            if nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[i] == 2:
                nums[i], nums[k] = nums[k], nums[i]
                # 注意i无需加1，因为这一步只是保证2到后面，并不能保证交换到i位置的数字不需要处理。
                k -= 1
            else:
                i += 1

