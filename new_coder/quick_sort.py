# quick sort
import random


def quick_sort(arr):
    quick_sort_r(arr, 0, len(arr) - 1)


def quick_sort_r(arr, p, r):
    if p > r:
        return

    q = partition(arr, p, r)
    quick_sort_r(arr, p, q - 1)
    quick_sort_r(arr, q + 1, r)


def partition(arr, p, r):
    i = j = p
    pivot_idx = random.randint(p, r)
    arr[r], arr[pivot_idx] = arr[pivot_idx], arr[r]
    pivot = arr[r]

    while i < r:
        if arr[i] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
        i += 1

    arr[j], arr[r] = arr[r], arr[j]
    return j


if __name__ == "__main__":
    arr = [9, 8, 8, 6, 2, 4, 6]
    quick_sort(arr)
    print(arr)
