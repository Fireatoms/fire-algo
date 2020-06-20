# min heap
# core operations
# 1. up to down heapify (on one tree node)
# 2. down to up heapify (on one tree node)
# 3. insert node to heap from tail
# 4. array to heap: 1. repeat 3(down to up) 2. up to down(last non-leaf node to first non-leaf node)
# 5. pop top node
# 6. heap sort
import time

def up(arr, idx):
    while (idx - 1) // 2 >= 0 and arr[(idx-1)//2] > arr[idx]:
        arr[(idx-1)//2], arr[idx] = arr[idx], arr[(idx-1)//2]
        idx = (idx-1) // 2


def down(arr, idx, n):
    """n代表树的节点个数"""
    while True:
        min_pos = idx
        if 2*idx+1 < n and arr[2*idx+1] < arr[idx]:
            min_pos = 2*idx+1
        if 2*idx+2 < n and arr[2*idx+2] < arr[min_pos]:
            min_pos = 2*idx+2
        if min_pos == idx:
            break

        arr[idx], arr[min_pos] = arr[min_pos], arr[idx]
        idx = min_pos


def insert(arr, val):
    arr.append(val)
    up(arr, len(arr) - 1)


def heapify_up(arr):
    """heapify: from down to up"""
    for idx in range(1, len(arr)):
        up(arr, idx)


def heapify_down(arr):
    n = len(arr)
    non_leaf = n // 2 - 1
    for idx in range(non_leaf, -1, -1):
        down(arr, idx, n)


def pop(arr):
    n = len(arr)
    if n == 0:
        return None

    val = arr[0]
    arr[0] = arr[n-1]
    arr.pop()

    if len(arr) != 0:
        down(arr, 0, len(arr))

    return val


def heap_sort(arr):
    n = len(arr)
    if n <= 1:
        return

    # heapify
    heapify_down(arr)

    while n > 1:
        arr[0], arr[n-1] = arr[n-1], arr[0]
        n -= 1
        down(arr, 0, n)


def reverse(arr):
    i, j = 0, len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


if __name__ == "__main__":
    arr = [33, 17, 22, 16, 13, 15, 21, 5, 6, 7, 8, 1, 2, 19]
    heap_sort(arr)
    print(arr)
    # using min heap to sort in place needs reverse arr at last
    arr.reverse()
    # reverse(arr)
    print(arr)

    # arr = [i for i in range(10)]
    # for i in range(10):
    #     print(pop(arr))
    # print(pop(arr))
    # arr = [2, 3, 1]
    # # down(arr, 0, 3)
    # up(arr, 2)
    # insert(arr, 1)
    # print(arr)
    # arr = [i for i in range(1000000, -1, -1)]
    # start_heapify_up = time.perf_counter()
    # heapify_up(arr)
    # end_heapify_up = time.perf_counter()
    # print("time elapse using up: {}".format(end_heapify_up - start_heapify_up))
    # arr = [i for i in range(1000000, -1, -1)]
    # start_heapify_down = time.perf_counter()
    # heapify_down(arr)
    # end_heapify_down = time.perf_counter()
    # print("time elapse using down: {}".format(end_heapify_down - start_heapify_down))