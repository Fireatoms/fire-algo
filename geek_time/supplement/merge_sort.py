# merge_sort


def merge_sort(nums):
    merge_sort_r(nums, 0, len(nums)-1)


def merge_sort_r(nums, p, r):
    if p >= r:
        return
    q = p + (r - p) // 2
    merge_sort_r(nums, p, q)
    merge_sort_r(nums, q+1, r)
    merge(nums, p, q, r)


def merge(nums, p, q, r):
    i, j, k = p, q + 1, 0
    tmp = [0] * (r - p + 1)
    while i <= q and j <= r:
        if nums[i] <= nums[j]:
            tmp[k] = nums[i]
            i += 1
        else:
            tmp[k] = nums[j]
            j += 1
        k += 1

    if i <= q:
        tmp[k:] = nums[i:q+1]
    else:
        tmp[k:] = nums[j:r+1]

    nums[p:r+1] = tmp[:]


if __name__ == "__main__":
    arr = [i for i in range(10, -1, -1)]
    merge_sort(arr)
    print(arr)