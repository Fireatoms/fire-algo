# link: https://leetcode-cn.com/problems/next-greater-element-iii/


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n_str = [int(c) for c in str(n)]
        length = len(n_str)

        i = length - 2
        while i >= 0 and n_str[i] >= n_str[i + 1]:
            i -= 1

        # desc
        if i < 0:
            return -1

        j = length - 1
        # boundary conditions
        while j >= 0 and n_str[j] <= n_str[i]:
            j -= 1

        n_str[i], n_str[j] = n_str[j], n_str[i]
        self.reverse(n_str, i + 1, length - 1)
        ans = int(''.join(map(str, n_str)))
        return ans if ans <= 2 ** 31 - 1 else -1

    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1


if __name__ == "__main__":
    num = 12
    sl = Solution()
    print(sl.nextGreaterElement(num))
