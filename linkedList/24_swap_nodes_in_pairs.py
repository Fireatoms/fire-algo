# link: https://leetcode.com/problems/swap-nodes-in-pairs/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        new_start = head.next.next
        tmp = head
        head = head.next
        head.next = tmp
        head.next.next = self.swapPairs(new_start)
        return head

    def swapPairsRe(self, head):
        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            first = cur.next
            second = cur.next.next
            cur.next = second
            first.next = second.next
            second.next = first
            cur = cur.next.next

        return dummy.next


def create_list(n):
    head = ListNode(1)
    list_node = head
    for i in range(2, n):
        list_node.next = ListNode(i)
        list_node = list_node.next

    return head


def print_list(head):
    while head:
        print(head.val)
        head = head.next

if __name__ == "__main__":
    head = create_list(6)
    sl = Solution()
    # head = sl.swapPairs(head)
    head = sl.swapPairsRe(head)
    print_list(head)