# link: https://leetcode-cn.com/problems/largest-number/


class LargerNumKey:
    def __init__(self, value, dd):
        self.value = value

    def __lt__(self, other):
        return self.value + other.value > other.value + self.value

    def __call__(self, *args, **kwargs):
        print('call')

class Solution:
    def largestNumber(self, nums):
        ans = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if ans[0] == '0' else ans


if __name__ == "__main__":
    arr = [10, 3, 20]
    sl = Solution()
    l = LargerNumKey(3)
    l1 = l()
    print(l == l1)
    print(sl.largestNumber(arr))