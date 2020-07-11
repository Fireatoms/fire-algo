# divide and conquer

# use merge sorting to calculate the num of reverse pair
from typing import List

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

# link: https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/
# tower of hanoi
"""
The pattern here is :
Shift 'n-1' disks from 'A' to 'B'.
Shift last disk from 'A' to 'C'.
Shift 'n-1' disks from 'B' to 'C'.
"""
class TowerOfHanoi:
    def __init__(self, n):
        self.__n = n
        self.__poles = [[i for i in range(n, 0, -1)], [], []]
        self.__from = 'A'
        self.__aux = 'B'
        self.__to = 'C'
        self.__poles_dict = {self.__from: 0, self.__aux: 1, self.__to: 2}

    def solve(self):
        self.process(self.__n)

    def process(self, n, from_rod='A', aux_rod='B', to_rod='C'):
        if n > 0:
            self.process(n-1, from_rod, to_rod, aux_rod)
            print('Move disk {} from rod {} to {}'.format(n, from_rod, to_rod))
            self.move(from_rod, to_rod)
            self.display_rods()
            self.process(n-1, aux_rod, from_rod, to_rod)
        else:
            return

    def move(self, source, destination):
        source_idx = self.__poles_dict[source]
        dest_idx = self.__poles_dict[destination]

        top = self.__poles[source_idx].pop()
        self.__poles[dest_idx].append(top)

    def display_rods(self):
        print('A: {} B: {} C: {}'.format(self.__poles[0], self.__poles[1], self.__poles[2]))


if __name__ == "__main__":
    th = TowerOfHanoi(3)
    th.solve()
    # crp = CalculateRversePairs()
    # re_num = crp.calculate_num([i for i in range(5, -1, -1)])
    # print('reverse pair nums: {}'.format(re_num))