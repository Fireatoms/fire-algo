#!/bin/python
# LRU淘汰算法本质上是一种存储策略，所以这里写一个lru的存储类即能做到承载改算法
# 使用的基本存储数据结构是数组


class ArrayLru:
    """
    底层的存储结构是数组
    """
    def __init__(self, capacity):
        self.__data = []
        # 容量和长度是独立两个概念，就像go里面的切片
        self._capacity = capacity

    def __len__(self):
        return len(self.__data)

    def search(self, value):
        for i in range(len(self)):
            if self.__data[i] == value:
                return i

        return -1

    def insert(self, value):
        value_index = self.search(value)
        if value_index != -1:
            # range(x, x)不进行操作，无需单独拿出来判断处理
            for i in range(value_index, len(self) - 1):
                self.__data[i] = self.__data[i + 1]
            self.__data[len(self) - 1] = value
        else:
            if len(self) < self._capacity:
                self.__data.append(value)
            else:
                for i in range(len(self)-1):
                    self.__data[i] = self.__data[i+1]
                self.__data[len(self)-1] = value

    def print_all(self):
        for v in self.__data:
            print(v)


def test_array_lru():
    array_lru = ArrayLru(5)
    array_lru.insert(1)
    array_lru.insert(2)
    array_lru.insert(3)
    array_lru.insert(4)
    array_lru.insert(5)
    array_lru.print_all()
    array_lru.insert(2)
    array_lru.print_all()
    array_lru.insert(6)
    array_lru.print_all()


if __name__ == "__main__":
    test_array_lru()