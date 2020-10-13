# link: https://leetcode-cn.com/problems/next-greater-element-iii/


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n_list = [int(c) for c in str(n)]
        n_length = len(n_list)

        i = n_length - 2
        while i >= 0 and n_list[i] >= n_list[i + 1]:
            i -= 1

        if i < 0:
            return -1

        j = n_length - 1
        while j >= 0 and n_list[j] <= n_list[i]:
            j -= 1

        n_list[i], n_list[j] = n_list[j], n_list[i]
        self.reverse(n_list, i + 1, n_length - 1)
        ans = int(''.join(map(str, n_list)))
        return ans if ans < 2 ** 31 - 1 else -1

    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1


if __name__ == "__main__":
    n = 12222333
    sl = Solution()
    print(sl.nextGreaterElement(n))