# 二分查找，时间复杂度o(logn)
# 包含以下内容
# 1. 迭代二分查找 2. 递归二分查找
# 二分查找变种：1. 查找第一个值等于给定值的元素  2. 查找最后一个值等于给定值的元素
# 3. 查找第一个大于等于给定值的元素  4. 查找最后一个小于等于给定值的元素


def binary_search(arr, value):
    """iteration"""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] < value:
            # low += 1 我总是下意识的想写成这个样子。干，一定要想清楚，保持清醒，没有一个点可以松懈
            low = mid + 1
        elif arr[mid] > value:
            # mid+1和mid-1的操作是为了防止陷入死循环，并且上面low<=high是为了保证每一个元素都被处理
            high = mid - 1
        else:
            return mid

    return -1


def binary_search_recursive(arr, value):
    return binary_search_rc(arr, 0, len(arr) - 1, value)


def binary_search_rc(arr, low, high, value):
    if low > high:
        return -1

    mid = low + (high - low) // 2
    if arr[mid] < value:
        return binary_search_rc(arr, mid + 1, high, value)
    elif arr[mid] > value:
        return binary_search_rc(arr, low, mid - 1, value)
    else:
        return mid


def test_binary_search():
    arr = list(3 * x for x in range(100))
    print(arr[9])
    print(binary_search(arr, 297))


def test_binary_search_rescursive():
    arr = list(3 * x for x in range(100))
    print(arr[9])
    print(binary_search(arr, 0))


if __name__ == "__main__":
    # test_binary_search()
    test_binary_search_rescursive()