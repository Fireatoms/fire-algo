class Node:
    """链表结点"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class SimpleSinglyLinkedList:
    """简易的单向链表, 带哨兵头结点"""

    def __init__(self):
        self.head = Node('SENTRY')

    def insert_to_tail(self, data):
        p = self.head
        while p.next is not None:
            p = p.next

        p.next = Node(data)

    def find_mid_node(self):
        """找中间结点
        注意：偶数时要找到靠后的那个结点：a->b->c->d,这个要找到的是c结点
        """
        slow = self.head.next
        fast = self.head.next

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        return slow


def reverse_from_node(node):
    """从node结点处开始翻转链表
    返回翻转后的第一个结点
    """
    pre = node
    cur = node.next
    # 这个是为了将起始结点变成尾结点（指向None的结点）
    pre.next = None
    while cur is not None:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp

    return pre


def is_palindrome(l):
    """检查存放在单向链表中的字符串是否是回文字符串
    1. 奇数：a->b->a, 找到中间值反转，后半部分：a->b->None，前半部分的a还是指向b，而此时b的指向已经变了：a->b->Node
    2. 偶数：a->b1->b2->a, b1和b2都代表b，等价，这里这么写单纯为了区分结点。要找到的中间结点是b2。反转，前半部分：a->b1
    后半部分a->b2->None
    3. 反转后，前后部分同时遍历，直到任意一个值为None
    4. 可以使用已有的singlyLinkedList，但这里为了多练习，依然选择再次实现一个单向链表
    """
    is_p = True
    mid = l.find_mid_node()
    back_node = reverse_from_node(mid)
    front_node = l.head.next

    while front_node is not None and back_node is not None:
        if front_node.data != back_node.data:
            is_p = False
            break

        front_node = front_node.next
        back_node = back_node.next

    return is_p


def test_is_p():
    l = SimpleSinglyLinkedList()
    p = 'abba'
    for c in p:
        l.insert_to_tail(c)
    print(is_palindrome(l))


if __name__ == "__main__":
    test_is_p()
