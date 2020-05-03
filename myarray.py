#!/bin/python
"""
python中列表实际上是数组容器类，支持动态扩容
这里利用列表构造原生的数组。模拟以下特性：
1.根据index获取value，指定index插入数据.但如果指定的index之前有空位置，会先将数据插入空位，保证内存连续
2.数组容量满了后，无法继续插入
3.删除或者插入元素，数据会发生数据迁移来保证内存的连续性
4.支持迭代遍历
5.可以使用python内置函数len获取数组长度
"""

class MyArray:
    def __init__(self, capacity: int):
        self._data = []
        self._capacity = capacity

    def __setitem__(self, key, value):
        self._data[key] = value

    def __getitem__(self, item):
        return self._data[item]

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        for item in self._data:
            yield item

    def find(self, index):
        try:
            return self._data[index]
        except IndexError:
            return None

    def delete(self, index):
        """
        数组元素删除后的数据搬移交给python的list容器去完成
        :param index:
        :return:
        """
        try:
            self._data.pop(index)
            return True
        except IndexError:
            return False

    def insert(self, index, value):
        if len(self) >= self._capacity:
            return False
        else:
            self._data.insert(index, value)
            return True

    # 额外一个数组全部元素的打印函数
    def print_all(self):
        for item in self:
            print(item)


def test_myarray():
    array = MyArray(5)
    array.insert(0, 3)
    array.insert(0, 4)
    array.insert(1, 5)
    array.insert(3, 9)
    array.insert(3, 10)
    array.print_all()
    # assert array.insert(0, 100) is False
    # assert len(array) == 5
    # assert array.find(1) == 5
    # assert array.delete(4) is True
    # array.print_all()


if __name__ == '__main__':
    test_myarray()