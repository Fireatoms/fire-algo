# merge sort


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
    tmp = [0] * (r - p + 1)
    i, j, k = p, q + 1, 0
    while i <= p and j <= r:
        if nums[i] <= nums[j]:
            tmp[k] = nums[i]
            i += 1
        else:
            tmp[k] = nums[j]
            j += 1
        k += 1

    start = i
    end = q
    if j <= r:
        start = j
        end = r

    while start <= end:
        tmp[k] = nums[start]
        k += 1
        start += 1
    nums[p:r+1] = tmp


if __name__ == "__main__":
    nums = [i for i in range(10, -1, -1)]
    merge_sort(nums)
    print(nums)