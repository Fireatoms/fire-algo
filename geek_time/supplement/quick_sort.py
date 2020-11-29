# quick sort
import random


def quick_sort(nums):
    quick_sort_r(nums, 0, len(nums)-1)


def quick_sort_r(nums, p, r):
    if p > r:
        return

    q = partition(nums, p, r)
    quick_sort_r(nums, p, q-1)
    quick_sort_r(nums, q+1, r)


def partition(nums, p, r):
    pivot_index = random.randint(p, r)
    nums[pivot_index], nums[r] = nums[r], nums[pivot_index]
    pivot = nums[r]

    i = j = p
    while j < r:
        if nums[j] <= pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1

    nums[i], nums[r] = nums[r], nums[i]
    return i


def quick_sort_iter(nums):
    stack = [0, len(nums)-1]
    while stack:
        high, low = stack.pop(), stack.pop()
        if high - low <= 0:
            continue

        pivot_index = partition(nums, low, high)
        stack.extend([low, pivot_index-1, pivot_index+1, high])


if __name__ == "__main__":
    nums = [i for i in range(10, -1, -1)]
    # quick_sort(nums)
    quick_sort_iter(nums)
    print(nums)