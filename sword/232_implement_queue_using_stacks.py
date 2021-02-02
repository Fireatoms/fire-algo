# link: https://leetcode-cn.com/problems/implement-queue-using-stacks/


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_push = []
        self.stack_pop = []
        self.front = -1

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.stack_push:
            self.front = x
        self.stack_push.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack_pop:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
        return self.stack_pop.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack_pop[-1] if self.stack_pop else self.front

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack_push and not self.stack_pop



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


if __name__ == "__main__":
    queue = MyQueue()
    for i in range(1, 4):
        queue.push(i)
    print(queue.peek())
    print(queue.pop())
    print(queue.peek())