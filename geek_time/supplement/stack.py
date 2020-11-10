# 基于数组实现的顺序栈与基于链表的链式栈
# 简化起见：栈中所有元素为正整数，返回-1代表未找到元素

class ArrayStack:
    def __init__(self, cap):
        self.__cap = cap
        self.__count = 0
        self.arr = [-1] * self.__cap

    def push(self, val):
        if self.__count >= self.__cap:
            return False
        self.arr[self.__count] = val
        self.__count += 1
        return True

    def pop(self):
        if self.__count == 0:
            return -1

        res = self.arr[self.__count-1]
        self.__count -= 1
        return res

    def top(self):
        if self.__count != 0:
            return self.arr[self.__count-1]
        return -1

    def __str__(self):
        elements = self.arr[:self.__count]
        return 'str' + '->'.join(map(str, elements))

    def __repr__(self):
        elements = self.arr[:self.__count]
        return 'repr' + '->'.join(map(str, elements))


class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class ListStack:
    def __init__(self, cap):
        self.cap = cap
        self.length = 0
        self.head = Node(-1)

    def push(self, val):
        if self.length >= self.cap:
            return False

        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return -1

        top_node = self.head.next
        self.head.next = self.head.next.next
        self.length -= 1
        return top_node.val

    def top(self):
        if self.length != 0:
            return self.head.next.val

        return -1

    def __str__(self):
        node_list = []
        node = self.head.next
        while node:
            node_list.append(node.val)
            node = node.next

        return "Nodes: " + "=>".join(map(str, node_list))


if __name__ == "__main__":
    # stack = ArrayStack(10)
    stack = ListStack(10)
    print(stack)
    for i in range(10):
        stack.push(i)

    print(stack.push(10))
    print(stack)
    print(stack.pop())
    print(stack.top())
    print(stack)

    res = stack.pop()
    while res >= 0:
        print(res)
        res = stack.pop()