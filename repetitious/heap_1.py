# max heap


def up(arr, idx):
    while (idx-1)//2 >= 0 and arr[idx] > arr[(idx-1)//2]:
        arr[idx], arr[(idx-1)//2] = arr[(idx-1)//2], arr[idx]
        idx = (idx-1)//2


def down(arr, idx, n):
    """n代表堆元素数量"""
    while True:
        max_pos = idx
        if 2*idx+1 < n and arr[2*idx+1] > arr[idx]:
            max_pos = 2*idx+1
        if 2*idx+2 < n and arr[2*idx+2] > arr[max_pos]:
            max_pos = 2*idx+2
        # 循环终止条件
        if max_pos == idx:
            break

        arr[idx], arr[max_pos] = arr[max_pos], arr[idx]
        idx = max_pos


def insert(arr, val):
    arr.append(val)
    up(arr, len(arr)-1)


def remove(arr, n):
    """声明：
    为了描述主体逻辑，这里实现的所有操作均未考虑异常情况
    """
    arr[0] = arr[n-1]
    arr.pop()
    down(arr, 0, len(arr))


def heapify_up(arr, n):
    for i in range(1, n):
        up(arr, i)


def heapify_down(arr, n):
    idx = n//2 - 1
    for i in range(idx, -1, -1):
        down(arr, i, n)


def arr_reverse(arr):
    """与主线无关，做一次原地的数组逆序"""
    low = 0
    high = len(arr) - 1
    while low < high:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1


def heap_sort(arr):
    n = len(arr)
    heapify_down(arr, n)

    while n > 1:
        arr[0], arr[n-1] = arr[n-1], arr[0]
        n -= 1
        down(arr, 0, n)


if __name__ == "__main__":
    arr = [33, 17, 22, 16, 13, 15, 21, 5, 6, 7, 8, 1, 2, 19]
    heap_sort(arr)
    print(arr)

    # arr = [i for i in range(11)]
    # arr_reverse(arr)
    # print(arr)

    # arr = [i for i in range(10)]
    # heapify_down(arr, len(arr))
    # print(arr)

    # arr = [i for i in range(10)]
    # heapify_up(arr, len(arr))
    # print(arr)

    # arr = [33, 17, 22, 16, 13, 15, 21, 5, 6, 7, 8, 1, 2, 19]
    # remove(arr, len(arr))
    # print(arr)

    # arr = [33, 17, 21, 16, 13, 15, 19, 5, 6, 7, 8, 1, 2]
    # insert(arr, 22)
    # print(arr)

    # arr = [2, 17, 21, 16, 13, 15, 19, 5, 6, 7, 8, 1]
    # down(arr, 0, len(arr))
    # print(arr)

    # arr = [33, 17, 21, 16, 13, 15, 19, 5, 6, 7, 8, 1, 2, 22]
    # up(arr, len(arr)-1)
    # print(arr)
