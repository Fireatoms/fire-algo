# link: https://leetcode.com/problems/remove-element/


class Solution:
    """写出这个双指针思路也不难，这样的交换次数会比较少
    此外还有两种：
    1. 逻辑非常简单，但是做了蛮多冗余的交换操作。如果是作为普通开发场景，简单意味着不容易出错，别人也好维护，也是不错的解法
    2. 逻辑也蛮巧妙，和我这个比起来条件判断更好，更好理解些
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        ln = len(nums)
        i = j = 0
        while j < ln:
            if nums[i] != val:
                i += 1
                j += 1
            else:
                if nums[j] != val:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
                else:
                    j += 1
        return i


class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:
        """我挺喜欢这个解法的，巨简单明了，就是有不必要的交换操作存在，当数据量比较大时性能会受影响，但我认为大部分场景下这样就足够了"""
        ln = len(nums)
        i = j = 0
        while j < ln:
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i


class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        # while i < j:
        # 一定要有=，因为每个数都应该得到处理
        while i <= j:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                i += 1

        return i