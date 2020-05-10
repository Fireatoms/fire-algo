# merge_sort，从上往下拆分问题，然后从下往上处理问题。不像快速排序是一边从上往下拆分问题，同时处理完问题
# 递推公式：merge_sort_c(arr, p, r) = merge(merge_sort_c(arr, p, q), merge_sort_c(arr, p+1, r))
# 终止条件：p >= r, q是中间点。注意在python3中，取整：q = (p+r)//2


def merge_sort(arr):
    merge_sort_c(arr, 0, len(arr)-1)


def merge_sort_c(arr, p, r):
    if p >= r:
        return
    q = (p+r) // 2
    merge_sort_c(arr, p, q)
    merge_sort_c(arr, q+1, r)
    # 处理好两个拆分问题后，进行数据合并
    # p => q, q+1 => r两部分排序
    merge(arr, p, q, r)


def merge(arr, p, q, r):
    # tmp = [None] * (r-q+1)
    tmp = [None] * (r-p+1)
    i = p
    j = q + 1
    # 临时数组的索引
    k = 0

    while i <= q and j <= r:
        # =判断条件是为了保持排序的稳定性
        if arr[i] <= arr[j]:
            tmp[k] = arr[i]
            i += 1
        else:
            tmp[k] = arr[j]
            j += 1
        k += 1

    start, end = i, q
    if j <= r:
        start, end = j, r

    while start <= end:
        tmp[k] = arr[start]
        k += 1
        start += 1

    # arr[p:r+1] = tmp # 感觉是比较像python风格的代码，也可以遍历求解
    for m in range(0, r-p+1):
        arr[p+m] = tmp[m]


if __name__ == '__main__':
    arr = list(range(5, -1, -1))
    merge_sort(arr)
    print(arr)