# link: https://leetcode-cn.com/problems/implement-queue-using-stacks/


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input_stack = []
        self.output_stack = []
        self.front = -1


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.input_stack:
            self.front = x
        self.input_stack.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())

        return self.output_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.output_stack[-1] if self.output_stack else self.front

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.input_stack and not self.output_stack



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()