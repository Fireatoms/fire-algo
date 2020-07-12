# insertion sort


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        value = arr[i]
        j = i - 1
        while j >= 0:
            if arr[j] > value:
                arr[j+1] = arr[j]
            else:
                break
            j -= 1

        arr[j+1] = value


if __name__ == "__main__":
    arr = [i for i in range(10, 0, -1)]
    print('before sorting: {}'.format(arr))
    insertion_sort(arr)
    print('after sorting: {}'.format(arr))