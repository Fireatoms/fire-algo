# link: https://leetcode.com/problems/implement-queue-using-stacks/


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._s1 = []
        self._s2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self._s1:
            self._s2.append(self._s1.pop())
        self._s1.append(x)

        while self._s2:
            self._s1.append(self._s2.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self._s1.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self._s1[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self._s1


class MyQueue1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._s1 = []
        self._s2 = []
        self._front = -1

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self._s1:
            self._front = x
        self._s1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self._s2:
            while self._s1:
                self._s2.append(self._s1.pop())
        return self._s2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self._s2:
            return self._s2[-1]

        return self._front

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not (self._s1 or self._s2)