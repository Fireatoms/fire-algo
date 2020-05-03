#!/bin/python

"""
刻意模拟下面的情况用于分析均摊时间复杂度：
往固定长度的数组中填入数据，当数据插满时，遍历数组计算加和，并将这个加和值放入数组第一个位置
"""
import  itertools

class DynamicArray:
    def __init__(self, length):
        self.length = length
        self.count = 0
        self.arr = [None] * self.length

    def insert(self, var):
        """
        模拟摊还时间复杂度的插入操作
        :param var:
        :return:
        """
        if self.count == len(self.arr):
            sum = 0
            for v in self.arr:
                sum += v
            self.arr[0] = sum
            self.count = 1
        self.arr[self.count] = var
        self.count += 1

    def add(self, var):
        """
        动态扩容数组，超限申请2倍的存储空间
        每n次插入出现一次全量复制，这个复制的时间复杂度是o(n)，摊还一下，整体的时间复杂度为o(1)
        :param var:
        :return:
        """
        if self.count >= self.length:
            self.length *= 2
            new_array = [None] * self.length
            for i in range(len(self.arr)):
                new_array[i] = self.arr[i]
            self.arr = new_array

        self.arr[self.count] = var
        self.count += 1


class Math:
    @staticmethod
    def factorial(number):
        if number == 0:
            return 1
        else:
            return number * Math.factorial(number - 1)


class MethodTypes:
    """
    The difference between the keywords self and cls reside only on the method type, on one hand if the created method
    is an instance method then the reserved word self have to be used, on the other hand if the method is a class method
    is a class method then the keyword cls must be used. Finally if the method is a static method then none of those words
     will be used because as said before static methods are self contained and do not have access to instance or
     class variables nor to instance or class methods.
    """

    name = "Ragnar"
    __secret_name = "Fire"
    _double = "Atom"

    def instanceMethod(self):
        # Creates an instance atribute through keyword self
        # self.lastname = "Lothbrock"
        self.name = "Man"
        print(self.name)
        # print(self.lastname)

    @classmethod
    def classMethod(cls):
        # Access a class atribute through keyword cls
        cls.name = "Lagertha"
        print(cls.name)

    @staticmethod
    def staticMethod():
        print("This is a static method")


class IterableContainer:
    """
    可迭代类
    """
    cdata = (3, 4, 5, 6)

    def __init__(self, data=(1, 2, 3, 4, 5)):
        self.data = data

    def __iter__(self):
        for x in self.data:
            yield x

    def print_all(self):
        for item in self:
            print(item)

    # 这个针对类方法的迭代函数写法实验起来有点问题，先放着
    # @classmethod
    # def __iter__(cls):
    #     for y in cls.cdata:
    #         yield y
    #
    # @classmethod
    # def print_class_all(cls):
    #     for y in cls:
    #         print(y)


class Fire:

    def __init__(self):
        self.__data = 1

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    def print_all(self):
        print(self.__data)


# yield
def foo():
    """
    https://blog.csdn.net/mieleizhi0522/article/details/82142856
    """
    print("starting...")
    while True:
        res = yield 4
        print("res:", res)


def add_foo(nf):
    if nf <= 1:
        return nf
    return add_foo(nf-1) + add_foo(nf-2)


def add_iter_foo(n):
    a = 0
    b = 1
    for j in range(n):
        a, b = b, a+b
    return b


def test_range():
    for i in range(1,1):
        print('range')

# def fab()

if __name__ == '__main__':
    # fire = Fire()
    # fire.print_all()
    # fire.data = 2
    # fire.print_all()
    # mt = MethodTypes()
    # print(mt.name)
    # # 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
    # print(mt._double)
    # # 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了
    # # print(mt.__secret_name)
    # test_range()
    # ic = IterableContainer()
    # # for i in ic:
    # #     print(i)
    # ic.print_all()
    # da = DynamicArray(5)
    # for i in range(11):
    #     da.add(i)
    # print(da.arr[5])
    # print(da.length)
    # # for i in range(da.length):
    # #     print(da.arr[i])
    #
    # factorial = Math.factorial(5)
    # print(factorial)
    #
    # # Creates an instance of the class
    # m = MethodTypes()
    # # Calls instance method
    # m.instanceMethod()
    #
    # # 这里改了一下类变量，后面所有这个类或者实例中name也变了，但是实例可以重置name值
    # MethodTypes.classMethod()
    # # MethodTypes.staticMethod()
    # m.instanceMethod()
    # n = MethodTypes()
    # print(n.name)
    # print(MethodTypes.name)
    #
    # # 私有变量外部无法访问
    # # print(MethodTypes.__secret_name)
    #
    # g = foo()
    # print(next(g))
    # print("*" * 20)
    # print(next(g))
    # print(g.send(7))
    #
    # print(add_foo(3))
    # print(add_iter_foo(3))
    # left = [0, 5, 1, 0, 1]
    # la = (left[i] for i, v in enumerate(left) if i % 2 == 1)
    # print(next(la))
    # print(next(la))
    # print(next(la, None))
    # seats = [0, 1, 1, 0, 0, 1, 0, 0, 1]
    # for seat, group in itertools.groupby(seats):
    #     # print(seat, group)
    #     print(seat, list(group))
    #
    # print(seats[::-2])
    # for i in range(5, -1, -1):
    #     print(i)
    #
    # for i in range(4):
    #     if i == 3:
    #         break
    # print('here', i)
    #
    # while None:
    #     print(4)

    st = 'ssfgv'
    for k,v in enumerate(st):
        print(k, v)

    for v in st:
        print(v)