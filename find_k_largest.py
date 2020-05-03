# 寻找数组中第k大的数据，要求O(n)的时间复杂度找到，可以利用快速排序使用的分区间方法.
# 这里面也有个前提，如果是已排好序的数组，这个时间复杂度会退化，问题规模变化: n + n-1 + n-2 + ... + 1
# 如果pivot选取得到，可以基本做到每次排序都将问题规模缩小一半，那问题的时间复杂度：n + n/2 + n/4 + .. +1
# 一样是递归的思想


def find_k_largest(arr, k):
    if k > len(arr) or k <= 0:
        return None
    return find_k_largest_c(arr, 0, len(arr)-1, k)


def find_k_largest_c(arr, p, r, k):
    q = partition(arr, p, r)
    if q == k - 1:
        return arr[q]
    elif q < k - 1:
        return find_k_largest_c(arr, q+1, r, k)
    else:
        return find_k_largest_c(arr, p, q-1, k)


def partition(arr, p, r):
    pivot = arr[r]
    i = j = p
    while j <= r-1:
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
    arr[i], arr[r] = arr[r], arr[i]

    return i


if __name__ == '__main__':
    arr = [2, 56, 5, 1, 6]
    print(find_k_largest(arr, 4))