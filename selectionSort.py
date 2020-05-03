# 链表选择排序
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkListWithHead:
    """带头（头一直指向哨兵结点）单向链表"""
    def __init__(self):
        self.head = Node(-1)

    def insert_to_tail(self, value):
        p = self.head
        while p.next is not None:
            p = p.next

        p.next = Node(value)

    def print_all(self):
        p = self.head.next
        while p is not None:
            print(p.value)
            p = p.next


def selection_sort_linked_list(lk):
    location_to_insert_pre = lk.head
    while location_to_insert_pre.next.next:
        min_node = compare_node = location_to_insert_pre.next
        min_node_pre = compare_node_pre = location_to_insert_pre
        while compare_node:
            if compare_node.value < min_node.value:
                min_node = compare_node
                min_node_pre = compare_node_pre
            compare_node_pre = compare_node
            compare_node = compare_node.next

        # 结点交换操作，逻辑是清晰的，步骤感觉蛮繁琐
        # 这里的交换逻辑是有问题的
        location_to_insert_after = location_to_insert_pre.next.next
        min_node_after = min_node.next
        location_to_insert = location_to_insert_pre.next
        location_to_insert_pre.next = min_node
        min_node.next = location_to_insert_after
        min_node_pre.next = location_to_insert
        location_to_insert.next = min_node_after

        # 循环自增条件
        location_to_insert_pre = location_to_insert_pre.next


def test_selection_sort_linked_list():
    lk = LinkListWithHead()
    for i in range(3, -1, -1):
        lk.insert_to_tail(i)

    print("Before sorting")
    lk.print_all()
    print("After sorting")
    selection_sort_linked_list(lk)
    lk.print_all()


# 选择排序
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == "__main__":
    # arr = [4, 5, 6, 3, 2, 1]
    # selection_sort(arr)
    # print(arr)
    # brr = [1]
    # selection_sort(brr)
    # print(brr)
    test_selection_sort_linked_list()