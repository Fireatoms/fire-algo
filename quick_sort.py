# 快速排序是从上往下进行排序操作，不断的选取参考点，将数组分散到参考点的左右
# 递推公式：quick_sort_c(arr, p, r) = quick_sort_c(arr, p, q-1) + quick_sort_c(arr, q+1, r)，注意这里的+不能简单理解成相加，理论上更像一个连接的意味
# 终止条件很好找：p >= r。指的注意的是分割点在q，这个q的左端都小于a[q],右端都大于a[q]


def quick_sort(arr):
    quick_sort_c(arr, 0, len(arr)-1)


def quick_sort_c(arr, p, r):
    if p >= r:
        return

    q = partition(arr, p, r)
    # quick_sort_c(arr, p, q),递推公式写错了，反应出来的是并没有真正理解，没有把递推公式和实际操作联系起来
    quick_sort_c(arr, p, q-1)
    quick_sort_c(arr, q+1, r)


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
    arr = [5, 6, 7, 1, 1, 3, 4, 2]
    quick_sort(arr)
    for v in arr:
        print(v)