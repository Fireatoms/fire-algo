# link: https://leetcode-cn.com/problems/largest-number/


class LargerNumKey(str):
    # little than, take effect when the operator is <
    def __lt__(self, other):
        return self + other > other + self


def large_num(x):
    return -x


class Solution:
    def largestNumber(self, nums):
        # largest_num = ''.join(sorted(map(str, nums), key=lambda x: LargerNumKey(x)))
        largest_num = ''.join(sorted(map(str, nums), key=lambda x: Test(x)))
        return '0' if largest_num[0] == '0' else largest_num


class TestCall(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print("self.name: %s. " % self.name, end='   ')
        print('__call__()  is  running ')


class Test:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    # greater than, take effect when the operator is >
    def __gt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def __le__(self, other):
        return self.value <= other.value

if __name__ == "__main__":
    test1 = Test(1)
    test2 = Test(2)
    print(test1 == test2)
    print(test1 == test2)
    print(test1 != test2)

    print(test1 <= test2)
    print(test1 >= test2)

    # arr = ['10', '2']
    # print(sorted(arr, key=LargerNumKey))

    # print(LargerNumKey(1) > LargerNumKey(2))
    # print(LargerNumKey(1) < LargerNumKey(2))

    # c = LargerNumKey(10)
    # print(type(c))
    # print(c + 'd')
    # d = str(10)
    # print(type(d), d)
    # nums = [10, 3]
    # sl = Solution()
    # print(sl.largestNumber(nums))

    # print(test1.__value2)

    # tc = TestCall('fang')
    # tc()

    # arr = [10, 9, 8]
    # print(sorted(arr, key=large_num))
    # print(sorted(arr, key=lambda x: -x))
