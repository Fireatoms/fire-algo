# link: https://leetcode-cn.com/problems/implement-stack-using-queues/v
from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue_store = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        length = len(self.queue_store)
        self.queue_store.append(x)
        for i in range(length):
            self.queue_store.append(self.queue_store.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue_store.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue_store[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue_store) <= 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


class MyStackAuxiliary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue_store = deque()
        self.queue_auxiliary = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue_auxiliary.append(x)
        while self.queue_store:
            self.queue_auxiliary.append(self.queue_store.popleft())
        self.queue_store, self.queue_auxiliary = self.queue_auxiliary, self.queue_store

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue_store.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue_store[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue_store) <= 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

class MyStackCap:

    def __init__(self, cap):
        """
        Initialize your data structure here.
        """
        self.queue_store = deque()
        self.queue_auxiliary = deque()
        self.cap = cap

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self.full():
            return

        self.queue_auxiliary.append(x)
        while self.queue_store:
            self.queue_auxiliary.append(self.queue_store.popleft())
        self.queue_store, self.queue_auxiliary = self.queue_auxiliary, self.queue_store

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty():
            return -1

        return self.queue_store.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue_store[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue_store) <= 0

    def full(self):
        return len(self.queue_store) >= self.cap

    def __len__(self):
        return len(self.queue_store)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()