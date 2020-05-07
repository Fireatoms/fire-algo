# 基于链表实现的链式队列长度很容易支持无限长度


class Node:
    """链表的基本组成结构：结点，老惯例了"""
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class ListQueueRe:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        """入队是从尾部操作，这里边界条件自然想到一tail做参照
        这里的判断是为了判断是否是空队列，空队列需要初始化，涉及head和tail的变动
        因为链表天然的可扩展性，这里没有判断队列是否满，真要限制，实际维护一个容量变量和当前队列长度来做
        """
        new_node = Node(value)
        if self.tail is None:
        # if self.head is None: 下面出队的tail清空部分注释掉，用这个判断，队列也能正常运行
            self.head = new_node
            self.tail = new_node

        self.tail.next = new_node
        self.tail = self.tail.next

    def dequeue(self):
        if self.head is None:
            return None
        v = self.head.value
        self.head = self.head.next
        if self.head is None:
            # 队列清空时，tail也要指向None,特别上面入队是用了tail判断是否需要初始化
            # 如果不做这个清空，上面入队时根据head是否为None来判断进行队列初始化也是可以的
            # 从对队列的理解上看这里做一次tail的清空更符合逻辑
            self.tail = None

        return v

    def print_all(self):
        p = self.head
        if p is None:
            print('queue empty')

        while p is not None:
            # tail的设置只是为了插入方便，实际队列中有哪些值，只需要head一直遍历到None即可
            print(p.value)
            p = p.next


def test_list_queue_re():
    lq = ListQueueRe()
    for i in range(3):
        lq.enqueue(i)

    lq.print_all()
    for i in range(4):
        print(lq.dequeue())

    lq.enqueue(5)
    lq.enqueue(6)
    lq.print_all()


if __name__ == "__main__":
    test_list_queue_re()