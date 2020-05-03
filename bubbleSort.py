class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListWithHead:
    """带哨兵头结点的链表"""
    def __init__(self):
        self.head = Node(-1)

    def insert_to_tail(self, value):
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(value)

    def print_all(self):
        p = self.head.next
        while p is not None:
            print(p.value)
            p = p.next


def bubble_sort_linked_list(lk):
    # f终止点，这个量的设置非常巧妙
    f = None
    head = lk.head
    while f != head.next.next:
        p = head
        while p.next.next != f:
            if p.next.value > p.next.next.value:
                x = p.next
                y = p.next.next
                x.next = y.next
                y.next = x
                p.next = y

            # 循环自增条件
            p = p.next
        f = p.next


def test_bubble_sort_linked_list():
    lk = LinkedListWithHead()
    for i in range(5, -1, -1):
        lk.insert_to_tail(i)
    lk.print_all()

    bubble_sort_linked_list(lk)
    lk.print_all()




# 经典的冒泡排序，n-1次循环，每次确定一个元素的￿最终位置
def bubble_sort(arr):
    n = len(arr)
    for i in range(1, n):
        # 标识是否发生交换
        flag = False
        for j in range(0, n-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True

        if not flag:
            break


def bubble_sort_reverse(arr):
    """从后往前挨个将元素放入正确位置
    没有特别意义，仅仅是为了训练思维
    """
    n = len(arr)
    for i in range(1, n):
        flag = False
        # 这里边界条件设置的下界结合实际过程反复理解下为什么是i-1,因为上界是一直n-1，下界每次要递增1，代表每次将一个元素放入低位的正确位置
        for j in range(n-1, i-1, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                flag =True

        if not flag:
            break


def test_bubble_sort():
    arr = [5,4,3,2,1,5]
    bubble_sort(arr)
    print(arr)


def test_bubble_sort_reverse():
    arr = [5, 4, 3, 2, 1, 5]
    bubble_sort_reverse(arr)
    print(arr)


if __name__ == "__main__":
    # test_bubble_sort()
    # test_bubble_sort_reverse()
    test_bubble_sort_linked_list()