# 1. 基于数组实现的静态栈
# 2. 基于链表实现的栈（这里不做容量限制）
# 3. 入栈出栈的时间复杂度O(1),如果是动态扩容的顺序栈（基于数组实现），则摊还时间复杂度也是O(1),n次入栈操作后才会出现一次
# 数据搬移


class ArrayStack:
    """
    1. 底层存储结构为数组
    2. 设置栈容量，超过容量则返回False禁止入栈
    顺序栈
    """

    def __init__(self, capacity):
        # 申请容量为capacity的数组作为存储
        self.data = [None] * capacity
        # 记录栈的容量
        self.cap = capacity
        # 记录当前栈中数据量
        self.count = 0

    def push(self, value):
        if self.count == self.cap:
            return False
        self.data[self.count] = value
        self.count += 1
        return True

    def pop(self):
        if self.count == 0:
            return None
        self.count -= 1
        return self.data[self.count]

    def print_all(self):
        for v in self.data:
            print(v)


class ArrayStackDynamic:
    """
    1. 底层存储结构为数组
    2. 当容量超限的时候自动扩容一倍
    """
    def __init__(self, capacity=1):
        # 初始化容量为capacity的数组作为存储
        self.data = [None] * capacity
        # 记录栈的容量
        self.cap = capacity
        # 记录当前栈中的数据量
        self.count = 0

    def push(self, value):
        """当超容量时，将底层数组扩容一倍"""
        if self.count == self.cap:
            data = self.data
            new_arr = [None] * 2 * self.cap
            for i in range(self.cap):
                new_arr[i] = data[i]
            self.data = new_arr
            self.data[self.count] = value
            self.count += 1
            self.cap *= 2
        else:
            # 一定要注意if和else的关系，有些为了简便直接省略了else，那么非else的部门是一定会执行的
            self.data[self.count] = value
            self.count += 1

    def pop(self):
        if self.count == 0:
            return None
        self.count -= 1
        return self.data[self.count]


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkListStack:
    """基于链表实现的链式栈
    1. 注意设置栈顶到链表头部，这一点对效率影响很大，就像用链表实现的lru淘汰算法，越早访问的放置到链表尾部
    2. 这里不做容量限制，只要内存足够就能插入数据
    3. 依然为了插入删除操作的简便性，引入哨兵结点
    """
    def __init__(self):
        # 设置哨兵头结点，这里如果设置成self.top=None，虽然需要处理None第一次插入的初始化问题，但从栈的概念上更好理解一些。
        self.head = Node(9999)

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head.next
        self.head.next = new_node

    def pop(self):
        if self.head.next is None:
            return None
        pop_node = self.head.next
        self.head.next = pop_node.next
        return pop_node.value

    def stack_top(self):
        if self.head.next is None:
            return None
        return self.head.next.value

    def clear_stack(self):
        """清空栈，模拟browser时使用，简单粗暴直接将哨兵结点指向None"""
        self.head.next = None

    def __repr__(self):
        p = self.head.next
        nums = []
        while p:
            nums.append(p.value)
            p = p.next

        return " ".join(f"{num}" for num in nums)


class Browser:
    """使用两个栈来模拟网页的前进和后退
    cur_stack存放当前显示网页及该网页前的浏览记录
    bak_stack存放当前网页之后的已浏览网页，如果新开网页，此栈中数据要清空
    forward: bak_stack中有网页才能向前，返回操作后的当前网页
    backward: cur_stack中至少有一个网页，可回退到最初状态：None。返回操作后的当前网页
    """
    def __init__(self):
        self.cur_stack = LinkListStack()
        self.bak_stack = LinkListStack()

    def open_new_page(self, value):
        self.bak_stack.clear_stack()
        self.cur_stack.push(value)

    def forward(self):
        bak_page = self.bak_stack.pop()
        if bak_page is None:
            return None
        self.cur_stack.push(bak_page)
        return bak_page

    def backward(self):
        for_page = self.cur_stack.pop()
        if for_page is None:
            return None
        self.bak_stack.push(for_page)
        return self.cur_stack.stack_top()


def test_browser():
    b = Browser()
    for i in "abc":
        b.open_new_page(i)
    print(b.backward())
    print(b.backward())
    print(b.backward())

    print(b.forward())
    print(b.forward())

    b.open_new_page('d')
    print(b.forward())
    print(b.backward())
    print(b.forward())


def calculate_stack(expression):
    """使用栈实现简易的运算式计算，仅支持+-*/四种运算符
    运算数栈，操作符栈。操作符入栈时：如果操作符优先级等于或小于栈顶操作符，则取出数栈和栈顶运算符进行运算
    """
    num_stack = LinkListStack()
    operator_stack = LinkListStack()
    op_priority = {'-': 0, '+': 0, '*': 1, '/': 1}
    for v in expression:
        if v in ['-', '+', '*', '/']:
            op_top = operator_stack.stack_top()
            while op_top is not None and op_priority[v] <= op_priority[op_top]:
                op_now = operator_stack.pop()
                n = num_stack.pop()
                m = num_stack.pop()
                r = execute(m, n, op_now)
                num_stack.push(r)
                op_top = operator_stack.stack_top()
            operator_stack.push(v)
        else:
            num_stack.push(int(v))
    n = num_stack.pop()
    m = num_stack.pop()
    op_now = operator_stack.pop()
    return execute(m, n, op_now)


def execute(m, n, op):
    if op == '+':
        result = m + n
    elif op == '-':
        result = m - n
    elif op == '*':
        result = m * n
    else:
        result = m / n
    return result


def is_bracket_match(brackets):
    """检验是否是匹配的括号对
    当前支持[ { (三种类型括号
    """
    bracket_stack = ArrayStackDynamic(5)
    bracket_map = {"[": "]", "{": "}", "(": ")"}
    is_matched = True
    for b in brackets:
        if b in bracket_map.keys():
            bracket_stack.push(b)
        else:
            # 右括号，不考虑非括号的异常情况
            l = bracket_stack.pop()
            if l is None or bracket_map[l] != b:
                is_matched = False
                break

    if is_matched:
        if bracket_stack.count != 0:
            is_matched = False

    return is_matched


def test_is_bracket_match():
    brackets = "{{{{{{}}}}"
    print(is_bracket_match(brackets))


def test_calculate_stack():
    expression = '3+5*8-6'
    print(calculate_stack(expression))


def test_stack():
    arr_stack = ArrayStack(5)
    for i in range(5):
        arr_stack.push(i)
    arr_stack.print_all()
    print(arr_stack.push(5))
    for i in range(6):
        print(arr_stack.pop())


def test_stack_dynamic():
    arr_stack_dynamic = ArrayStackDynamic(5)
    for i in range(6):
        arr_stack_dynamic.push(i)
    for i in range(6):
        print(arr_stack_dynamic.pop())


def test_link_stack():
    link_stack = LinkListStack()
    for i in range(5):
        link_stack.push(i)

    # print(link_stack)
    print(link_stack.stack_top())


if __name__ == '__main__':
    # test_stack()
    # test_link_stack()
    # test_stack_dynamic()
    # test_calculate_stack()
    # test_is_bracket_match()
    test_browser()