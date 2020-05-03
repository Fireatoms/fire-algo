# 分治的思想，通过递归来实现分治
# 递推公式：merge_sort_c(p, r) = merge(merge_sort_c(p, q), merge_sort_c(q+1, r))，q是p到r的中间值，q = (q+r)//2, 终止条件是p>=r
# 递推公式中参数是实际的索引值。比如长度为n的数组，索引为0 - n-1
# 遭遇代码奇奇怪怪的逻辑时，先找是不是有上下界条件写错了。比如我这里r-p+1开始写成了r-q+1, 这个问题是真的难发现


def merge_sort(arr):
    merge_sort_c(arr, 0, len(arr)-1)


def merge_sort_c(arr, p, r):
    if p >= r:
        return

    q = (p + r) // 2
    merge_sort_c(arr, p, q)
    merge_sort_c(arr, q+1, r)
    merge(arr, p, q, r)


def merge(arr, p, q, r):
    """p到q，q+1到r索引分别是两段已经排好序的部分"""
    tmp = [None] * (r - p + 1)
    i = p
    j = q + 1
    k = 0

    while i <= q and j <= r:
        # 判断条件带=是为了排序的稳定性
        if arr[i] <= arr[j]:
            tmp[k] = arr[i]
            k += 1
            i += 1
        else:
            tmp[k] = arr[j]
            k += 1
            j += 1

    start = i
    end = q
    if j <= r:
        start = j
        end = r

    while start <= end:
        #脑子要活，不要一按次数循环就只想到range
        tmp[k] = arr[start]
        k += 1
        start += 1

    for m in range(r-p+1):
        arr[p+m] = tmp[m]


if __name__ == '__main__':
    arr = [2, 2, 1]
    merge_sort(arr)
    for v in arr:
        print(v)
