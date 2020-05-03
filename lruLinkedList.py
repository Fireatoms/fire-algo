import singlyLinkedList


class LruLinkedList:
    """基于链表实现的lru存储，基于单链表
    1. 本质上是存储，所以要规定容量，链表只是数据组织形式
    2. 越早插入的数据越靠近尾部，这样设计的原因是为了插入时不用遍历到尾部
    3. 插入结点不存在：链表满了，则删除尾部，将新结点插入头部。链表没满，直接插入头部
    3. 如果插入的结点已存在，则从原来位置
    4. 简便起见：存储int类型或者字符类型
    5. 引入的单链表应用了哨兵头结点简化操作
    """

    def __init__(self, capacity):
        self.data = singlyLinkedList.SinglyLinkedList()
        self.capacity = capacity
        self.length = 0

    def insert(self, value):
        pre_node, node = self.data.find_by_value(value)

        if node is None:
            if self.length < self.capacity:
                # 存储未满，直接插入到头部
                self.data.insert_to_head(value)
                self.length += 1
            else:
                # 存储已满，删除最末尾数据，再插入新结点到头部
                self.data.delete_last_n_node(1)
                self.data.insert_to_head(value)
        else:
            # 从原位置删除
            pre_node.next_node = node.next_node
            self.data.insert_to_head(value)

    def print_all(self):
        self.data.print_all()


def test_lru():
    ll = LruLinkedList(5)
    for i in range(5):
        ll.insert(i)

    ll.print_all()
    print('********')
    ll.insert(9)
    ll.print_all()
    print('********')
    ll.insert(2)
    ll.print_all()
    print('********')
    ll.insert(1)
    ll.print_all()


if __name__ == '__main__':
    test_lru()