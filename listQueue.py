# 设置头指针与尾指针
# 头指针为了出队方便，尾指针为了入队方便。可以想象即使没有头尾指针，仅仅使用链表也能模拟入队和出队的操作


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedListQueue:
    """设置头和尾结点，不特意设置哨兵结点，这里哨兵并未带来概念和操作上便利
    基于链表实现，就不做容量限制
    头和尾指针均向实际队列中的结点，这一点和数组实现的队列不同。数组实现的队列，尾指针指向的是队列最后一个结点的下一个位置
    这里面的异同思想还要好好体会下：数组是有容量的，链表末尾很好判断指向None。数组很难的明确表示末尾。
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # 习惯上还是要写全if else，写习惯省略else后很容易把需要else处理的情况写到默认要处理的块上去了
            self.tail.next = new_node
            self.tail = self.tail.next

    def dequeue(self):
        if self.head is None:
            return None

        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None

        return value

    def print_all(self):
        p = self.head
        while p is not None:
            print(p.value)
            p = p.next


def test_linked_list_queue():
    lq = LinkedListQueue()
    for i in range(3):
        lq.enqueue(i)

    lq.print_all()
    for i in range(2):
        print(lq.dequeue())

    lq.enqueue(5)
    lq.enqueue(6)
    lq.print_all()


if __name__ == "__main__":
    test_linked_list_queue()
