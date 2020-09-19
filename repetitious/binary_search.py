# binary search recursive
count = 0


def binary_search(nums, target):
    return binary_search_r(nums, 0, len(nums) - 1, target)


def binary_search_r(nums, low, high, target):
    global count
    if low > high:
        return -1

    mid = low + (high - low) // 2
    if nums[mid] > target:
        count += 1
        return binary_search_r(nums, low, mid - 1, target)
    elif nums[mid] < target:
        count += 1
        return binary_search_r(nums, mid + 1, high, target)
    else:
        return mid


if __name__ == "__main__":
    nums = [i for i in range(1000)]
    print(binary_search(nums, 88))
    print(count)