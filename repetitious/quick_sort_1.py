# 排序流程：不断的选择pivot，然后小于pivot的放到左端，大于等于pivot的放在右边，当排序区间缩小到1时，说明数组有序了
# 模拟这个过程的递推公式：quick_sort_c(arr, p, r) = quick_sort_c(arr, p, q-1) + quick_sort_c(arr, q+1, r)
# 其中q代表pivot所在位置，问题就被划分成p -> q-1 和 q+1 -> r的两个子问题。递归的退出条件是区间缩小为1，也即p >= r
# 注意上面提到的区间均是闭区间

def quick_sort_1(arr):
    quick_sort_1_c(arr, 0, len(arr)-1)


def quick_sort_1_c(arr, p, r):
    if p >= r:
        return

    q = partition(arr, p, r)
    quick_sort_1_c(arr, p, q-1)
    quick_sort_1_c(arr, q+1, r)


def partition(arr, p, r):
    pivot = arr[r]
    i = j = p
    while j <= r - 1:
        # if arr[i] < pivot: 为什么会犯这个错误？是不是偷懒靠印象速记了一些东西？
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1

    arr[i], arr[r] = arr[r], arr[i]
    return i


if __name__ == '__main__':
    arr = [5, 6, 7, 1, 1, 3, 4, 2]
    quick_sort_1(arr)
    for v in arr:
        print(v)