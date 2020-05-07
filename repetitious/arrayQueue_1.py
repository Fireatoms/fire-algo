# 基于数组实现的队列
# 1. tail指针指向最后一个元素之后，教程指导这么干
# 2. tail指针指向最后一个元素
# 理解倒是很好理解，可是一段时间不想，自己下意识的去实现的话，会优先想到上面第二种的指向规则
# 3. 考虑清楚下面几件事情，实现就问题不大：
# 队列的基本元素，底层存储结构：数组，队列容量，头指针，尾指针
# 入队操作，入队时判断是否队满，出队操作，出队判断是否队空
# 考虑正常的入队操作，然后分离出需要特殊处理的情况：这里是tail指向末尾，需要整体做数据搬移的情况


class ArrayQueueRe:
    def __init__(self, cap):
        self.cap = cap
        self.data = [None] * cap
        self.head = 0
        self.tail = 0

    def enqueue(self, value):
        # 返回值代表是否入队成功
        if self.tail == self.cap:
            if self.head == 0:
                return False
            # 数据整体前移head位置
            for i in range(self.head, self.tail):
                self.data[i - self.head] = self.data[i]
            # 数据搬完后还要记得指针重置
            self.tail -= self.head
            self.head = 0

        # 这里统一做入队赋值操作
        self.data[self.tail] = value
        self.tail += 1
        return True

    def dequeue(self):
        # 返回真实值与空None
        if self.head == self.tail:
            return None
        v = self.data[self.head]
        self.head += 1
        return v

    def print_all(self):
        """额外的打印函数，方便校验队列操作是否正确"""
        for i in range(self.head, self.tail):
            print(self.data[i])


class ArrayQueueTailRe:
    """这个类，将tail指针指向最后一个元素，复杂度增加，纯粹为了做思维训练，以后写队列还是要用上面的方式
    队空：head > tail
    队满：head = 0 tail = n - 1
    """
    def __init__(self, cap):
        self.cap = cap
        self.data = [None] * cap
        self.head = 0
        self.tail = -1

    def enqueue(self, value):
        if self.tail == self.cap - 1:
            if self.head == 0:
                return False
            for i in range(self.head, self.tail + 1):
                self.data[i-self.head] = self.data[i]
            self.tail -= self.head
            self.head = 0

        self.data[self.tail+1] = value
        self.tail += 1
        return True

    def dequeue(self):
        if self.head > self.tail:
            return None
        v = self.data[self.head]
        self.head += 1
        return v


class CircularQueueRe:
    """基于数组的循环队列是为了避免数据搬移
    这个时候tail指向末尾后一位的便利性就展现出来（）
    考虑关键点：
    队满：(tail+1)%n = head
    队空：head = tail
    另外注意下head的自增不是单纯的自增就够，还要有取余运算
    """
    def __init__(self, cap):
        self.cap = cap
        self.data = [None] * cap
        self.head = 0
        self.tail = 0

    def enqueue(self, value):
        if (self.tail + 1) % self.cap == self.head:
            return False
        self.data[self.tail] = value
        self.tail = (self.tail + 1) % self.cap
        return True

    def dequeue(self):
        if self.head == self.tail:
            return None
        v = self.data[self.head]
        self.head = (self.head + 1) % self.cap
        return v

    def print_all(self):
        head = self.head
        tail = self.tail
        while head != tail:
            print(self.data[head])
            head = (head + 1) % self.cap


def test_circular_queue_re():
    cq = CircularQueueRe(3)
    for i in range(3):
        print(cq.enqueue(i))

    print("first queue: ")
    cq.print_all()
    print("first dequeue: ")
    print(cq.dequeue())
    print(cq.dequeue())
    print(cq.dequeue())
    print(cq.head, cq.tail)
    cq.enqueue(4)
    print("second queue: ")
    cq.print_all()
    print("dequeue")
    for i in range(3):
        print(cq.dequeue())
    print(cq.head, cq.tail)


def test_array_queue_re():
    aq = ArrayQueueRe(3)
    for i in range(4):
        print(aq.enqueue(i))
    aq.print_all()
    print("dequeue: ")
    print(aq.dequeue())
    print(aq.dequeue())
    aq.enqueue(4)
    print("en: ")
    aq.print_all()
    # 纯粹为了看出搬移的过程
    print("底层数据：")
    for i in aq.data:
        print(i)


def test_array_queue_tail_re():
    aq = ArrayQueueRe(3)
    for i in range(4):
        print(aq.enqueue(i))
    aq.print_all()
    print("dequeue: ")
    print(aq.dequeue())
    print(aq.dequeue())
    aq.enqueue(4)
    print("en: ")
    aq.print_all()
    # 纯粹为了看出搬移的过程
    print("底层数据：")
    for i in aq.data:
        print(i)


if __name__ == '__main__':
    # test_array_queue_re()
    # test_array_queue_tail_re()
    test_circular_queue_re()