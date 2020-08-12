# link: https://leetcode.com/problems/min-stack/
"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__data = []
        self.__min = []

    def push(self, x: int) -> None:
        if not self.__data:
            self.__min.append(x)
        else:
            if x < self.__min[-1]:
                self.__min.append(x)
            else:
                self.__min.append(self.__min[-1])

        self.__data.append(x)

    def pop(self) -> None:
        if not self.__data:
            return None

        self.__data.pop()
        self.__min.pop()

    def top(self) -> int:
        return self.__data[-1]

    def getMin(self) -> int:
        return self.__min[-1]


# more concise
class MinStack1:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__data = [(None, float('inf'))]

    def push(self, x: int) -> None:
        self.__data.append((x, min(x, self.__data[-1][1])))

    def pop(self) -> None:
        if len(self.__data) > 1:
            self.__data.pop()

    def top(self) -> int:
        return self.__data[-1][0]

    def getMin(self) -> int:
        return self.__data[-1][1]
