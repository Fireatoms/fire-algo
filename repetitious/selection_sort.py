# selection sort


def selection_sort(arr):
    for i in range(0, len(arr)-1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[min_idx], arr[i] = arr[i], arr[min_idx]


if __name__ == "__main__":
    arr = [i for i in range(10, 0, -1)]
    print('before sorting: {}'.format(arr))
    selection_sort(arr)
    print('after sorting: {}'.format(arr))