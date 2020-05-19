# link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers, target):
        """
        这个题限定了一定有且只有一组解，这个问题就极大的简化了
        """
        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return [i+1, j+1]

    def sum_target_nums(self, arr, target):
        """
        来个复杂点的，计算加和等于target的组合数
        数组中数据可以重复
        举例：1 2 2 2 2 3 target:4 则有6对，组合数
        1 2 2 3 3 4 targe: 5 则有4对，2*2
        """
        i, j = 0, len(arr) - 1
        nums = 0
        while i < j:
            if arr[i] + arr[j] < target:
                i += 1
            elif arr[i] + arr[j] > target:
                j -= 1
            else:
                i_value = arr[i]
                j_value = arr[j]
                i_num = 0
                j_num = 0
                if i_value == j_value:
                    nums += ((j-i+1)*(j-i)) // 2
                    return nums

                while arr[i] == i_value:
                    i_num += 1
                    i += 1

                while arr[j] == j_value:
                    j_num += 1
                    j -= 1

                nums += i_num * j_num

        return nums

    def sum_target_nums_unique(self, arr, target):
        """
        相比上面的求解，这里规定相同的数字对只计算一次
        """
        i, j = 0, len(arr) - 1
        nums = 0
        while i < j:
            if arr[i] + arr[j] < target:
                i += 1
            elif arr[i] + arr[j] > target:
                j -= 1
            else:
                i_value = arr[i]
                j_value = arr[j]
                if i_value == j_value:
                    nums += 1
                    return nums

                while arr[i] == i_value:
                    i += 1

                while arr[j] == j_value:
                    j -= 1

                nums += 1

        return nums


if __name__ == "__main__":
    sc = Solution()
    arr = [1, 2, 2, 2, 3, 3, 4]
    print(sc.sum_target_nums(arr, 4))
    print(sc.sum_target_nums_unique(arr, 4))
