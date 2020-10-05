# link: https://leetcode-cn.com/problems/implement-queue-using-stacks/


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        self.front = 0


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.stack1:
            self.front = x
        self.stack1.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack2[-1] if self.stack2 else self.front


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not (self.stack1 or self.stack2)



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()