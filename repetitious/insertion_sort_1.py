# when the data size is small, insertion sort is efficient enough


def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = i - 1
        while j >= 0:
            if val < arr[j]:
                arr[j+1] = arr[j]
            else:
                break

            j -= 1

        arr[j+1] = val


if __name__ == "__main__":
    arr = [i for i in range(10, -1, -1)]
    insertion_sort(arr)
    print(arr)