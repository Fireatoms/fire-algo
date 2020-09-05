# counting sort


def counting_sort(nums):
    if not nums:
        return nums

    max_num = max(nums)
    nc = [0] * (max_num+1)
    for n in nums:
        nc[n] += 1

    for i in range(1, len(nc)):
        nc[i] = nc[i-1] + nc[i]

    tmp = [0] * len(nums)
    for i in range(len(nums)-1, -1, -1):
        idx = nc[nums[i]] - 1
        tmp[idx] = nums[i]
        nc[nums[i]] = idx

    nums[:] = tmp


if __name__ == "__main__":
    nums = [i for i in range(10, -1, -1)]
    counting_sort(nums)
    print(nums)