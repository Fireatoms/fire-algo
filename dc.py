# divide and conquer

# use merge sorting to calculate the num of reverse pair


class CalculateRversePairs:
    def __init__(self):
        self.__num = 0

    def calculate_num(self, arr):
        self.mergesort_r(arr, 0, len(arr) - 1)
        return self.__num

    def mergesort_r(self, arr, p, r):
        if p >= r:
            return
        q = (r - p) // 2 + p
        self.mergesort_r(arr, p, q)
        self.mergesort_r(arr, q+1, r)
        self.merge(arr, p, q, r)

    def merge(self, arr, p, q, r):
        i, j, k = p, q+1, 0
        tmp = [None] * (r-p+1)

        while i <= q and j <= r:
            if arr[i] <= arr[j]:
                tmp[k] = arr[i]
                k += 1
                i += 1
            else:
                self.__num += q - i + 1
                tmp[k] = arr[j]
                k += 1
                j += 1

        start = i
        end = q
        if j <= r:
            start = j
            end = r

        while start <= end:
            tmp[k] = arr[start]
            start += 1
            k += 1

        arr[p:r+1] = tmp


if __name__ == "__main__":
    crp = CalculateRversePairs()
    re_num = crp.calculate_num([i for i in range(5, -1, -1)])
    print('reverse pair nums: {}'.format(re_num))