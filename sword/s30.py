# link: https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/
import math


class MinStackTwo:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = [math.inf]
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(self.min_stack[-1], x))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.min_stack[-1]


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_val = -1

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min_val = x
        else:
            diff = x - self.min_val
            if diff < 0:
                self.min_val = x
            self.stack.append(diff)

    def pop(self) -> None:
        diff = self.stack.pop()
        if diff <= 0:
           self.min_val = self.min_val - diff

    def top(self) -> int:
        return self.min_val if self.stack[-1] <= 0 else self.stack[-1] + self.min_val

    def min(self) -> int:
        return self.min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()


if __name__ == '__main__':
    ms = MinStack()
    ms.push(1)
    # print(ms.min())
    ms.push(2)
    # print(ms.min())
    # ms.push(-3)
    print(ms.stack, ms.min_val)
    ms.pop()
    print(ms.stack, ms.min_val)
    print(ms.top())