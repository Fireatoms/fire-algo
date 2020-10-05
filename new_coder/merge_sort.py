# merge sort


def merge_sort(arr):
    merge_sort_r(arr, 0, len(arr) - 1)


def merge_sort_r(arr, p, r):
    if p >= r: # 这里一定是要有 = 作为退出判断的，因为下面的merge_sort_r(arr, p, q)会陷入死循环
        return

    q = p + (r - p) // 2
    merge_sort_r(arr, p, q)
    merge_sort_r(arr, q + 1, r)
    merge(arr, p, q, r)


def merge(arr, p, q, r):
    tmp = [0] * (r - p + 1)
    i, j, k = p, q + 1, 0

    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp[k] = arr[i]
            i += 1
        else:
            tmp[k] = arr[j]
            j += 1
        k += 1

    start = i
    end = q

    if start > end:
        start = j
        end = r

    tmp[k:] = arr[start:end+1]
    arr[p:r+1] = tmp


    # while start <= end:
    #     tmp[k] = arr[start]
    #     k += 1
    #     start += 1
    #
    # k = 0
    # while p <= r:
    #     arr[p] = tmp[k]
    #     p += 1
    #     k += 1


if __name__ == "__main__":
    arr = [9, 4, 5, 6, 9, 2]
    merge_sort(arr)
    print(arr)