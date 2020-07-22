# lru cache based on array


class LruCacheBasedOnArr(object):
    def __init__(self, cap):
        self.__cap = cap
        self.__data = [None] * self.__cap
        self.__length = 0

    def __len__(self):
        return self.__length

    def insert(self, val):
        if val in self.__data:
            idx = self.__data.index(val)
            self.shift_backforward(0, idx, self.__data)
            self.__data[0] = val
        else:
            if self.is_full():
                self.shift_backforward(0, self.__length-1, self.__data)
            else:
                self.shift_backforward(0, self.__length, self.__data)
                self.__length += 1
            self.__data[0] = val

    def is_full(self):
        return self.__length >= self.__cap

    def search(self, val):
        # change the cache order
        if val not in self.__data:
            return False

        idx = self.__data.index(val)
        self.shift_backforward(0, idx, self.__data)
        self.__data[0] = val

    def print_all(self):
        """
        just for testing
        :return:
        """
        print(self.__data)

    @staticmethod
    def shift_backforward(start, end, l):
        for i in range(end, start, -1):
            l[i] = l[i-1]


if __name__ == "__main__":
    lc = LruCacheBasedOnArr(3)
    for i in range(10):
        lc.insert(i)
    lc.print_all()
    lc.search(8)
    lc.print_all()