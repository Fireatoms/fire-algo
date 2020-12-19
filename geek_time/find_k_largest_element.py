#!/usr/bin/env python
import random


class Solution:
    def find_k_largest_element(self, arr, k):
        if k < 1 or k > len(arr):
            return -1
        return self.quick_sort(arr, 0, len(arr) - 1, k)

    def quick_sort(self, arr, p, r, k):
        if p > r:
            return

        q = self.partition(arr, p, r)
        if q == k - 1:
            return arr[q]
        elif q > k - 1:
            return self.quick_sort(arr, p, q - 1, k)
            # self.quick_sort(arr, p, q - 1, k)
        else:
            # self.quick_sort(arr, q + 1, r, k)
            return self.quick_sort(arr, q + 1, r, k)

    def partition(self, arr, p, r):
        pivot = random.randint(p, r)
        arr[pivot], arr[r] = arr[r], arr[pivot]
        pivot_val = arr[r]

        i, j = p, p
        while j < r:
            if arr[j] >= pivot_val:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
            j += 1

        arr[i], arr[r] = arr[r], arr[i]
        return i


if __name__ == "__main__":
    sl = Solution()
    arr = [i for i in range(1000)]
    print(sl.find_k_largest_element(arr, 1))