# 1. 大顶堆


class Heap:
    """实现的是一个大顶堆"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        # 位置0不存放数据，数据从1开始存放
        # 此种情况下i结点的父结点：i/2, i结点左子结点：2i, 右子结点：2*i + 1
        self.data = [None] * (capacity + 1)

    def insert_node(self, value):
        if self.count >= self.capacity:
            return
        self.count += 1
        self.data[self.count] = value

        # 从下往上进行堆化操作
        i = self.count
        while (i//2) > 0 and self.data[i//2] < value:
            self.data[i//2], self.data[i] = self.data[i], self.data[i//2]
            i //= 2

    def remove_root(self):
        """对于大顶堆来说，删除根结点即代表删除最大结点"""
        if self.count == 0:
            return
        self.data[1] = self.data[self.count]
        self.count -= 1
        self.heapify(1, self.data, self.count)

    def heapify(self, h_index, arr, n):
        """将索引h_index的结点从上往下进行堆化"""
        # 比较复杂一些，需要找到左右子结点中较大的点，并且该子结点的值大于当前结点值
        while True:
            max_pos = h_index
            if (2 * h_index) <= n and arr[2*h_index] > arr[h_index]:
                max_pos = 2 * h_index
            # 看下面这个错误的写法，实际开发过程中其实蛮容易出现这种错误的
            # 用上一个if语句中产生的max_pos来做比较才是这个地方的精髓所在
            # if (2 * h_index + 1) <= n and arr[2*h_index+1] > arr[h_index]:
            if (2 * h_index + 1) <= n and arr[2*h_index+1] > arr[max_pos]:
                max_pos = 2 * h_index + 1
            if max_pos == h_index:
                break
            arr[h_index], arr[max_pos] = arr[max_pos], arr[h_index]
            h_index = max_pos

    def build_heap(self, arr, n):
        """这个堆化的逻辑是处理一整个数组，从上到下进行堆化，实际单独出来成为非类函数，直接对已有数据进行处理更合适"""
        # 传参数组，即其容量使该函数适用性更好，可以处理外部传入的数组进行排序操作
        for idx in range(n//2, 0, -1):
            self.heapify(idx, arr, n)

    def heap_sort(self, arr, n):
        self.build_heap(arr, n)
        # 每次堆化如果还是用n做总体长度，那么排序算法就会失效
        # k = n
        # while k > 1:
        #     arr[1], arr[n] = arr[n], arr[1]
        #     self.heapify(arr, n)
        #     k -= 1

        k = n
        while k > 1:
            arr[1], arr[k] = arr[k], arr[1]
            k -= 1
            self.heapify(1, arr, k)

    def print_all(self):
        print(self.data[1:self.count+1])


def test_heap_sort():
    # 0号索引不存放数据，所以如果要排序数组，索引0位置的数据不参与排序
    # 所以堆里面实际数据是9, 8, 7, 6, 5, 4, 3, 2, 1, 0
    arr = [i for i in range(10, -1, -1)]
    hp = Heap(0)
    print("before: ")
    print(arr)
    hp.heap_sort(arr, len(arr) - 1)
    print("after: ")
    print(arr)


def test_heap_insert():
    hp = Heap(10)
    for i in range(10):
        hp.insert_node(i)
    hp.print_all()


def test_remove_root():
    hp = Heap(10)
    for i in range(10):
        hp.insert_node(i)
    print("删除前：")
    hp.print_all()
    hp.remove_root()
    print('删除后：')
    hp.print_all()
    for i in range(10):
        hp.remove_root()
    print("删除所有的根结点：")
    hp.print_all()


if __name__ == "__main__":
    # test_heap_insert()
    # test_remove_root()
    test_heap_sort()