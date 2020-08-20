# merge sort
def merge_sort(arr):
    l = len(arr)
    merge_sort_r(arr, 0, l-1)


def merge_sort_r(arr, p, r):
    if p >= r:
        return

    q = (p + r) // 2
    merge_sort_r(arr, p, q)
    merge_sort_r(arr, q+1, r)
    merge(arr, p, q, r)


def merge(arr, p, q, r):
    assist_list = [None] * (r - p + 1)
    i = p
    j = q + 1
    k = 0

    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            assist_list[k] = arr[i]
            i += 1
        else:
            assist_list[k] = arr[j]
            j += 1
        k += 1

    start = i
    end = q

    if j <= r:
        start = j
        end = r

    while start <= end:
        assist_list[k] = arr[start]
        start += 1
        k += 1

    for i in range(r-p+1):
        arr[p+i] = assist_list[i]


if __name__ == "__main__":
    arr = [i for i in range(10, -1, -1)]
    merge_sort(arr)
    print(arr)