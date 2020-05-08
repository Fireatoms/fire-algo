# link: https://leetcode.com/problems/rotate-array/


class Solution:
    """暴力解法：时间复杂度很高，很容易超限（k接近n时，O(n2)）"""
    def rotate(self, nums, k: int) -> None:
        for i in range(k):
            self.rotate_one(nums)

    def rotate_one(self, nums):
        ln = len(nums)
        value = nums[ln-1]
        for i in range(ln-1, 0, -1):
            nums[i] = nums[i-1]
        nums[0] = value


class Solution1:
    """这就是典型的拿空间换时间，通过n的空间，将时间复杂度控制在O(n)，优于上面的暴力解法近o(n2)的时间复杂度"""
    def rotate(self, nums, k: int) -> None:
        ln = len(nums)
        tmp = [None] * ln
        for i in range(ln):
            tmp[(i+k)%ln] = nums[i]
        nums[:] = tmp

def test_rotate():
    rs = Solution()
    nums = [1, 2, 3, 4, 5]
    rs.rotate(nums, 3)
    print(nums)


class Solution2:
    """根据变化的逻辑找规律，时间复杂度o(n),空间复杂度o(1)"""
    def rotate(self, nums, k: int) -> None:
        ln = len(nums)
        k = k % ln
        self.reverse(nums, 0, ln-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, ln-1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1



if __name__ == '__main__':
    rs2 = Solution2()
    nums = [1, 2, 3, 4, 5]
    rs2.rotate(nums, 3)
    print(nums)