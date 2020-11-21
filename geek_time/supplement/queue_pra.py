class ArrayQueue:
    def __init__(self, cap):
        self.items = [0] * cap
        self.cap = cap
        self.length = 0
        self.head = 0
        self.tail = 0

    def enqueue(self, val):
        if self.tail == self.cap:
            if self.head == 0:
                return False

            for i in range(self.head, self.tail):
                self.items[i - self.head] = self.items[i]

            self.tail -= self.head
            self.head = 0
            # head变了，这里我错过很多很多次了
            # self.head -= self.head
            # self.tail -= self.head

        self.items[self.tail] = val
        self.tail += 1
        self.length += 1

    def dequeue(self):
        if self.head == self.tail:
            return

        ret = self.items[self.head]
        self.head += 1
        self.length -= 1
        return ret

    def peek(self):
        return self.items[self.head] if self.length > 0 else None

    def __len__(self):
        return self.length


class ArrayQueueRepe:
    def __init__(self, cap):
        self.cap = cap
        self.items = [0] * self.cap
        self.head = 0
        self.tail = 0

    def enqueue(self, val):
        if self.tail == self.cap:
            if self.head == 0:
                return False

            for i in range(self.head, self.tail):
                self.items[i-self.head] = self.items[i]

            self.tail -= self.head
            self.head = 0

        self.items[self.tail] = val
        self.tail += 1
        return True

    def dequeue(self):
        if self.head == self.tail:
            return

        res = self.items[self.head]
        self.head += 1
        return res

    def peek(self):
        return self.items[self.head] if self.head != self.tail else None

    def __len__(self):
        return self.tail - self.head


class CycleArrayQueue:
    # real capacity: cap - 1
    def __init__(self, cap):
        self.cap = cap
        self.items = [0] * self.cap
        self.head = 0
        self.tail = 0
        self.length = 0

    def enqueue(self, val):
        if (self.tail + 1) % self.cap == self.head:
            return False

        self.items[self.tail] = val
        self.tail = (self.tail + 1) % self.cap
        self.length += 1

    def dequeue(self):
        if self.head == self.tail:
            return

        res = self.items[self.head]
        self.head = (self.head + 1) % self.cap
        self.length -= 1
        return res

    def peek(self):
        return self.items[self.head] if self.head != self.tail else None

    def __len__(self):
        return self.length


if __name__ == "__main__":
    # array_queue = ArrayQueueRepe(5)
    array_queue = CycleArrayQueue(6)
    for i in range(5):
        array_queue.enqueue(i)

    print(array_queue.items)
    print(len(array_queue))

    array_queue.enqueue(5)
    print(array_queue.peek())
    print(array_queue.items)

    for i in range(6):
        print(array_queue.dequeue())

    print(array_queue.items)
    print(array_queue.peek())
    print(array_queue.head, array_queue.tail)

    for i in range(3):
        array_queue.enqueue(i+3)

    print(array_queue.items, array_queue.head, array_queue.tail)

    print(array_queue.dequeue())
    print(array_queue.items, array_queue.head, array_queue.tail)
    print(array_queue.enqueue(9))
    print(array_queue.items, array_queue.head, array_queue.tail)
    print(len(array_queue))
    for i in range(len(array_queue)+1):
        print(array_queue.dequeue())

    print(array_queue.items, array_queue.head, array_queue.tail)
