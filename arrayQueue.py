# 基于数组实现的非循环队列
# 基于数组实现的循环队列


class ArrayQueue:
    """
    底层数据存储结构为数组，不支持动态扩容，限定容量，队满后禁止入队
    队列核心元素：队列容量，队头指针（指向队头数据），队尾指针（指向下一个入队位置），底层存储数组
    """

    def __init__(self, capacity):
        self.data = [None] * capacity
        self.cap = capacity
        # 队头和队尾指针有些微妙的差别，初始化指向同一个点，代表队列为空（是队列是否为空的判断依据）
        self.head = 0
        self.tail = 0

    def dequeue(self):
        if self.head == self.tail:
            return None
        ret = self.data[self.head]
        self.head += 1
        return ret

    def enqueue(self, value):
        """队满的条件是tail指向末尾，head指向0
        tail指向队尾n，但head不为0时需要先做数据搬移再进行入队操作
        正常的入队操作：数据入队，tail往后推1位
        """
        if self.tail == self.cap:
            if self.head == 0:
                return False
            # 数据搬移
            for i in range(self.head, self.tail):
                self.data[i-self.head] = self.data[i]

            # 不要忘记指针也要匹配变动,还有变动的前后顺序，head和tail变动的顺序先前写错了
            self.tail -= self.head
            self.head = 0

        self.data[self.tail] = value
        self.tail += 1
        return True

    def print_all(self):
        for i in range(self.head, self.tail):
            # 这个仅仅是为了打印验证数据，并且循环条件的设置保证了head=tail时不返回数据，也即队列为空
            print(self.data[i])


def test_array_queue():
    aq = ArrayQueue(3)
    for i in range(4):
        print(aq.enqueue(i))
    aq.print_all()
    print("dequeue: ")
    print(aq.dequeue())
    print(aq.dequeue())
    aq.enqueue(4)
    print("en: ")
    aq.print_all()
    print("底层数据：")
    for i in aq.data:
        print(i)


class CircularQueue:
    """基于数组实现的循环队列，head指向队列内元素，tail指向队内最后一个元素的下一个位置
    队空条件：head = tail
    队满条件：(tail+1)%c = head, 画图就很明确了，因为是环形，日常容量取模即可
    """
    def __init__(self, capacity):
        self.cap = capacity
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0

    def enqueue(self, value):
        # 判断队满,队满则入队失败。从这个条件可以发现循环队列有一个位置是不存放数据的。也即当tail指向head的前一个位置时
        if (self.tail + 1) % self.cap == self.head:
            return False
        self.data[self.tail] = value
        self.tail = (self.tail + 1) % self.cap
        return True

    def dequeue(self):
        # 判断队空，队空返回None
        if self.head == self.tail:
            return None
        value = self.data[self.head]
        self.head = (self.head + 1) % self.cap
        return value

    def print_all(self):
        head = self.head
        tail = self.tail
        while head != tail:
            print(self.data[head])
            head = (head + 1) % self.cap


def test_circular_queue():
    cq = CircularQueue(3)
    for i in range(3):
        print(cq.enqueue(i))

    print("first queue: ")
    cq.print_all()
    print("first dequeue: ")
    print(cq.dequeue())
    cq.enqueue(4)
    print("second queue: ")
    cq.print_all()


if __name__ == "__main__":
    # test_array_queue()
    test_circular_queue()