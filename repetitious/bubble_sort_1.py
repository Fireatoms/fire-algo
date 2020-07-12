# bubble sort


def bubble_sort(arr):
    n = len(arr)

    for i in range(1, n):
        is_ordered = True
        for j in range(n - i):
            if arr[j] > arr[j+1]:
                is_ordered = False
                arr[j], arr[j+1] = arr[j+1], arr[j]

        if is_ordered:
            return


if __name__ == "__main__":
    arr = [i for i in range(10, 0, -1)]
    print('before sorting: {}'.format(arr))
    bubble_sort(arr)
    print('after sorting: {}'.format(arr))