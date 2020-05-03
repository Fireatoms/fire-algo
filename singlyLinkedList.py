# 1.单链表结构及相关插入删除操作
# 2.基本组成数据结构是结点
# 3.简便起见，链表中存放的是int类型数据或字符串类型


class Node:
    """链表结构的Node结点"""

    def __init__(self, data, next_node=None):
        """
        Node结点初始化方法：
        data:存储的int类型数据
        next:下一个结点的引用地址
        """
        self.__data = data
        self.__next = next_node

    # 下面要实现的是Node下的数据获取更改，next指针获取修改动作

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next_node(self):
        return self.__next

    @next_node.setter
    def next_node(self, next_node):
        self.__next = next_node


class SinglyLinkedList:
    """单向链表"""

    def __init__(self):
        """设置哨兵头结点，简化特殊情况下的插入删除操作"""
        # 头结点指针永远指向这个哨兵结点
        self.__head = Node(9999)

    @property
    def head(self):
        return self.__head

    def find_by_value(self, value):
        """
        根据数据值在链表中查找
        额外返回一个前序结点
        :param value:
        :return:
        """
        node = self.__head
        pre_node = None
        while (node is not None) and (node.data != value):
            pre_node = node
            node = node.next_node
        return pre_node, node

    def find_by_index(self, index):
        """按照索引值在链表中查找"""
        pos = 0
        node = self.__head
        while (node is not None) and (pos != index):
            node = node.next_node
            pos += 1
        return node

    def insert_after(self, node, value):
        """在某个结点后添加值为value的结点"""
        new_node = Node(value)
        new_node.next_node = node.next_node
        node.next_node = new_node

    def insert_to_head(self, value):
        """插入结点到头部"""
        new_node = Node(value)
        new_node.next_node = self.head.next_node
        self.head.next_node = new_node

    def insert_to_tail(self, value):
        """插入值为value的新结点到链表的末尾"""
        new_node = Node(value)
        node = self.__head
        while node.next_node is not None:
            node = node.next_node

        node.next_node = new_node

    def find_node_before(self, node):
        """寻找给定结点的前序结点"""
        p = self.__head
        not_found = False # 记录是否找到前序结点
        while p.next_node != node:
            if p.next_node is None:
                not_found = True
                break
            else:
                p = p.next_node

        if not not_found:
            return p.next_node
        return None


    def insert_before(self, node, value):
        """在某个结点前插入结点
        1.当指定的结点不存在时，返回false提示没有指定的结点
        2.插入成功返回True
        """
        node_before = self.find_node_before(node)
        if node_before is not None:
            new_node = Node(value)
            new_node.next_node = node
            node_before.next_node = new_node
            return True

        return False

    def delete_by_node(self, node):
        """删除给定结点
        1. 没找到结点则返回False
        2. 找到则删除并返回True
        """
        node_before = self.find_node_before(node)
        if node_before is not None:
            node_before.next_node = node.next_node
            return True

        return False

    def delete_by_value(self, value):
        """找到给定值的结点，进行删除"""
        # 特意修改了按值找结点的函数，让其可以返回前序结点
        pre_node, node = self.find_by_value(value)
        if node is not None:
            pre_node.next_node = node.next_node
            return True

        return False

    def delete_last_n_node(self, n):
        """删除倒数第n个结点
        实现思路：
            设置快慢两个指针，快指针先行n-1步，指向正数第n个结点。
            启动慢指针，快指针继续移动到最后一个结点，慢指针同步移动，最终慢指针会指向倒数第n个结点
        """
        slow = self.__head
        fast = self.__head
        pre_node = self.__head

        for num in range(n-1):
            fast = fast.next_node

        while fast.next_node is not None:
            pre_node = slow
            fast = fast.next_node
            slow = slow.next_node

        pre_node.next_node = slow.next_node

    def find_mid_node(self):
        """寻找链表的中间结点
        实现思路：
           快慢指针，快指针每次移动两个位置，慢指针移动一个位置
           当快指针移动到尾结点或倒数第二个结点时，慢指针指向中间结点
           注意引入了哨兵结点，所以指针的头指向的并不是链表的第一个结点，所以遍历的边界条件要注意做些调整
           这个找到的中间结点是偶数链表的靠前的那个结点：x->a->b->c->d,会找到b，但判断回文字符串时，希望找到的是后面那个中间结点
           这一点在做回文字符串判断时要注意
        """
        fast = self.__head
        slow = self.__head

        while fast is not None and fast.next_node is not None:
            fast = fast.next_node.next_node
            slow = slow.next_node

        return slow

    def reverse_self(self):
        """
        翻转链表，我这里引入了哨兵头结点，这个反转的函数要考虑到哨兵的存在
        实际的操作原理是不断的交换结点对的位置
        :return:
        """
        pre = self.__head.next_node
        # 当链表中没有结点（除去哨兵结点）或只有一个结点是，无需反转操作
        if pre is None or pre.next_node is None:
            return
        cur = pre.next_node
        pre.next_node = None # 这里特别注意，第一个结点经过翻转后会变成最后被一个结点，所以需要将其后序结点变为None，否则成了循环链表
        while cur is not None:
            pre, cur = self.reverse_two_nodes(pre, cur)

        # 恢复哨兵
        self.__head.next_node = pre

    def reverse_two_nodes(self, pre, cur):
        """翻转两个结点，并且返回下一对需要反转的结点"""
        # 存放反转到前面去的结点的next结点，此结点后续要被反转到前面，以此类推，找到这个结点的后序结点
        tmp = cur.next_node
        cur.next_node = pre
        # cur变成新的pre，准备和tmp（原始指向的后序结点）
        # 当tmp为None时，说明无需再做翻转
        pre = cur
        cur = tmp

        return pre, cur

    def print_all(self):
        node = self.__head
        while node.next_node is not None:
            node = node.next_node
            print(node.data)

    def cycle_detect(self):
        """检查链表中是否有环
        1. 没有：返回None
        2. 有：返回环入口结点
        """
        fast = self.__head
        slow = self.__head
        has_cycle = False
        encounter = None

        while fast is not None and fast.next_node is not None:
            fast = fast.next_node.next_node
            slow = slow.next_node
            if fast == slow:
                has_cycle = True
                encounter = fast
                break # 经常忘记这个循环跳出导致死循环

        if has_cycle:
            p = self.__head
            q = encounter
            while p != q:
                p = p.next_node
                q = q.next_node

            return p

        return None

    def insert_tail_node(self, node):
        """将尾结点指向指定结点
        1. 我写这个方法是为了方便构造一个环出来：指向一个链表中已存在的结点
        2. 上面有个创建指定值结点并插入到链表尾部的方法
        """
        p = self.__head
        while p.next_node is not None:
            p = p.next_node

        p.next_node = node


def merge_ordered_linklist(lkm, lkn):
    """两个有序链表的合并
    思路：
    1. 当做将一个链表插入到另一个链表
    2. 以lkm为基准，循环检测，当lkn的结点小于lkm时，将lkn中结点小于lkm时
    将lkn中结点加入lkm结点之前
    """
    # 有了哨兵方便很多，所有要操作的结点都有前序结点，无需对第一个结点进行特殊处理
    pp = lkm.head
    qp = lkn.head
    p = pp.next_node
    q = qp.next_node

    while p is not None or q is not None:
        # 边界退出条件，必有一个成立
        if p is None:
            pp.next_node = q
            break
        if q is None:
            break

        if p.data >= q.data:
            # 插入成立条件，此时p不动，q继续往后寻找结点进行插入操作
            qa = q.next_node
            pp.next_node = q
            q.next_node = p
            pp = q
            q = qa
            continue

        pp = p
        p = p.next_node


def test_merge_ordered_linklist():
    """构造如下两个链表：
    lkm: 1->3->5->7
    lkn: 4->6->7
    """
    lkm = SinglyLinkedList()
    lkm.insert_to_tail(1)
    lkm.insert_to_tail(3)
    lkm.insert_to_tail(5)
    lkm.insert_to_tail(7)

    lkn = SinglyLinkedList()
    lkn.insert_to_tail(4)
    lkn.insert_to_tail(6)
    lkn.insert_to_tail(7)

    merge_ordered_linklist(lkm, lkn)
    lkm.print_all()


def test_cycle_detect():
    sl = SinglyLinkedList()
    for i in range(5):
        sl.insert_to_tail(i)
    ec = sl.find_by_index(2)
    print(ec.data)
    sl.insert_tail_node(ec)
    print(sl.cycle_detect().data)


if __name__ == "__main__":
    # test_cycle_detect()
    test_merge_ordered_linklist()