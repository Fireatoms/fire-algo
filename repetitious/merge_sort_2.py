# 继续重复练习
# 递推公式：merge_sort_r(arr, p, r) = merge(merge_sort_r(arr, p, q), merge_sort_r(arr, q+1, r)) 其中：q = (p+r) / 2


def merge_sort(arr):
    merge_sort_r(arr, 0, len(arr) - 1)


def merge_sort_r(arr, p, r):
    # 大声告诉我，一般步骤是什么？当然是考虑递归终止条件，不然不就无限进行，导致内存溢出了
    if p >= r:
        return

    q = (p + r) // 2
    # 下面这三行实际上就是递推公式的实现，先merge_sort_r进行排序处理，然后merge函数将两个排好序的部分进行合并
    # 对应到问题拆解与合并这两个过程上去
    merge_sort_r(arr, p, q)
    merge_sort_r(arr, q + 1, r)
    merge(arr, p, q, r)


def merge(arr, p, q, r):
    i = p
    j = q + 1
    k = 0
    tmp = [None] * (r - p + 1)

    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp[k] = arr[i]
            i += 1
        else:
            tmp[k] = arr[j]
            j += 1

        k += 1

    # 处理没有插入到临时数组中的部分
    start = i
    end = q
    if j <= r:
        start = j
        end = r

    while start <= end:
        tmp[k] = arr[start]
        start += 1
        k += 1

    # for m in range(r - p + 1):
    #     arr[p + m] = tmp[m]
    # 用一个更像python风格的方式进行赋值
    arr[p:r+1] = tmp


if __name__ == '__main__':
    arr = list(range(5, -1, -1))
    merge_sort(arr)
    print(arr)